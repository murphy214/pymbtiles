import json


def blank_geojson(geom_type,coordinates):
    return {"geometry": {"type": geom_type.encode('utf-8'), "coordinates": coordinates}, "type": "Feature", "properties": {}}

# creates a new geoijson point featuer
def new_point(point):
    return blank_geojson('Point',point)

# creates a new geoijson point featuer
def new_multipoint(points):
    return blank_geojson('MultiPoint',points)

# creates a new geoijson point featuer
def new_line(line):
    return blank_geojson('LineString',line)
# creates a new geoijson point featuer
def new_multiline(lines):
    return blank_geojson('LineString',lines)

# creates a new geoijson point featuer
def new_polygon(line):
    return blank_geojson('Polygon',line)
# creates a new geoijson point featuer
def new_multipolygon(lines):
    return blank_geojson('MultiPolygon',lines)


