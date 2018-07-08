import sqlite3
import math
from vector_tile_pb2 import Tile
from geojson import new_line,new_multiline,new_point,new_multipoint,new_polygon,new_multipolygon
import json

POINT = 1
LINESTRING = 2
POLYGON = 3

'''
converts raw bytes to a tile
'''
def read_tile_pbf(rawbytes):
    return Tile().FromString(rawbytes)

'''
delta dim converts the delta encoding
'''
def deltadim(num):
    return float(((num >> 1) ^ (-(num & 1))))

'''
projects a line into coordinate space
'''
def project(line, x0, y0, size):
    for j,p in enumerate(line):
        y2 = 180 - (p[1]+y0)*360.0/size
        line[j] = [(p[0]+x0)*360.0/size - 180.0,360.0/math.pi*math.atan(math.exp(y2*math.pi/180.0)) - 90.0]
    return line

# signed area frunction
def signedarea(ring):
	sumval = 0.0
	i = 0
	lenn = len(ring)
	j = lenn - 1
	p1, p2 = [],[]
	while i < lenn:
		if i != 0:
			j = i - 1
		p1 = ring[i]
		p2 = ring[j]
		sumval += (p2[0] - p1[0]) * (p1[1] + p2[1])
		i+=1
	return sumval

''' 
spings up polygons based on a flat list of lines
'''
def create_polygons(lines,geom_type):
    if geom_type == POLYGON:
        '''
        generalized polygon logic 
        '''
        polygons = []
        if len(lines) == 1:
            polygons.append(lines)
        else:
            for line in lines:
                if len(line) > 0:
                    val = signedarea(line)
                    if val < 0:
                        polygons.append([line])
                    else:
                        if len(polygons) == 0:
                            polygons.append([line])

                        else:
                            polygons[len(polygons)-1].append(line)
    else:
        return [lines]

'''
converts a protobuf vector tile value to a regular python pritivee
'''
def get_value(value):
	typeval = value.ListFields()[0][0].__dict__['json_name']
	if typeval == 'boolValue':
		return value.bool_value
	elif typeval == 'doubleValue':
		return value.double_value
	elif typeval == 'floatValue':
		return value.float_value
	elif typeval == 'intValue':
		return value.int_value
	elif typeval == 'sintValue':
		return value.sint_value
	elif typeval == 'stringValue':
		return str(value.string_value).encode('utf-8')
	elif typeval == 'uintValue':
		return value.uint_value

'''
returns geojson features from a tile
'''
def read_tile_features(tile,xyz):    
    x,y,z = xyz
    total_features = []
    for layer in tile.layers:
        if layer.extent == 0:
            layer.extent = 4096
        
        # getting projection properties
        size = float(layer.extent) *  math.pow(2, float(z))
        x0 = float(layer.extent * x)
        y0 = float(layer.extent * y)

        # getting keys,values from layer
        values = [get_value(i) for i in layer.values]
        keys = [i.encode('utf-8') for i in layer.keys]
    
        for feature in layer.features:
            lines = []
            currentpt = [0.0,0.0]
            pos = 0
            while pos < len(feature.geometry):
                if feature.geometry[pos] == 9:
                    currentpt = [
                        round(deltadim(feature.geometry[pos+1]) + currentpt[0],7),
                        round(deltadim(feature.geometry[pos+2]) + currentpt[1],7)
                    ]
                    line = [currentpt]
                    pos += 3
                    val = feature.geometry[pos]
                    pos += 1
                    length = val >> 3
                    length = length * 2
                    while pos < pos + length  and pos < len(feature.geometry):
                        currentpt = [
                            round(deltadim(feature.geometry[pos]) + currentpt[0],7),
                            round(deltadim(feature.geometry[pos+1]) + currentpt[1],7)
                        ]
                        line.append(currentpt)
                        pos += 2

                    lines.append(line)
                    line = []
                elif feature.geometry[pos] == 15:
                    pos+=1
            
            # adding whats left of the potential line
            if len(line) > 0:
                lines.append(line)
            
            # creating polygons
            polygons = create_polygons(lines,feature.type)
            
            # converting polygon
            for i in range(len(polygons)):
                for j in range(len(polygons[i])):
                    polygons[i][j] = project(polygons[i][j],x0,y0,size)

            # creating features
            if feature.type == POINT:
                if len(polygons[0][0]) == 1:
                    newfeature = new_point(polygons[0][0][0])
                else:
                    newfeature = new_multipoint(polygons[0][0])
            elif feature.type == LINESTRING:
                # projecting each possible line    
                if len(polygons[0]) == 1:
                    new_feature = new_line(polygons[0][0])
                else:
                    new_feature = new_multiline(polygons[0])
            elif feature.type == POLYGON:
                if len(polygons):
                    new_feature = new_polygon(polygons[0])
                else:
                    new_feature = new_multipolygon(polygons)

            new_feature['properties'] =  {keys[feature.tags[i*2]]:values[feature.tags[i*2+1]] for i in range(len(feature.tags)/2)}
            new_feature['properties']['layer'] = layer.name.encode('utf-8')
            
            total_features.append(new_feature)

    return total_features

'''
The mbtiles structure
'''
class Mbtiles():
    def __init__(self,filename,conn):
        self.conn = conn
        self.filename = filename
        self.cursor = conn.cursor()


    '''
    queries a single tile and returns the raw bytes

    '''
    def query(self,*varints):
        x,y,z = varints
        y = (1 << int(z)) - 1 - int(y)   
        self.cursor.execute('select tile_data from tiles where zoom_level = ? and tile_column = ? and tile_row = ?', (z,x,y))
        value = self.cursor.fetchone()
        if value == None:
            return ''
        else:
            return value[0]
    
    '''
    returns a raw structured bytes
    '''
    def get_tile(self,*varints):
        return read_tile_pbf(self.query(*varints))

    '''
    from a raw tile returns geojson features
    '''
    def get_features(self,*varints):
        return read_tile_features(read_tile_pbf(self.query(*varints)),varints)

'''
creating a new mbtiles structure from a filename
'''
def new_mbtiles(filename):
    conn = sqlite3.connect(filename)
    return Mbtiles(filename,conn)
