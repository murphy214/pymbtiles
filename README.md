# pymbtiles

#### Caveats 

Hasn't been tested thoroughly on polygons and multi-polygons but if there is something wrong its a simple fix. (this was ported from golang) Pythons gzip libary implementation is pretty fucked (takes a file reader / writer) and I don't feel like looking up how to mask byte arrays in iostream at the moment so that currently isn't supported either but easily could be.

# Example 

```python
import pymbtiles

# creaing mbtiles file
mbtile = pymbtiles.new_mbtiles('wv_roads12.mbtiles')

# x,y,z
print mbtile.get_features(1112,1576,12)[:4]

'''
OUTPUT
[{'geometry': {'type': 'LineString', 'coordinates': [[-82.25366990198381, 38.25537100105143], [-82.25327900145203, 38.255611003744946], [-82.25296810094733, 38.25575700341881], [-82.25271010072902, 38.25591500656728], [-82.25202090397943, 38.25623600583944], [-82.25178590160795, 38.25636000023192], [-82.25141110480763, 38.256597601396294]]}, 'type': 'Feature', 'properties': {'layer': 'Test', 'District': 2.0, 'Route': 1675.0, 'Label': '1675', 'ROUTEID': '0601675000000', 'BMP': 0.0, 'SuppCode': 0.0, 'EMP': 0.14946641503913702, 'ONEWAY': False, 'Shape_Leng': 240.474179907, 'SubRoute': 0.0, 'CountyCode': 6.0, 'SignSystem': 0.0, 'StreetName': 'UPPER BOWEN CREEK RD'}}, {'geometry': {'type': 'LineString', 'coordinates': [[-82.24671590316575, 38.26942200374731], [-82.24671790434513, 38.26934550317327], [-82.2467489016708, 38.269194500674615], [-82.2467489016708, 38.269081509767034], [-82.24672590382397, 38.26896950168049], [-82.24662890424952, 38.268723501160025], [-82.24647601309698, 38.26837750483625], [-82.24634500395041, 38.2680005029832], [-82.24620301451068, 38.2676625030621], [-82.24613201455213, 38.26753150700179], [-82.24607500713319, 38.26744750635817], [-82.24593091174029, 38.2673095012706], [-82.24580191425048, 38.26721850817418], [-82.24562000075821, 38.26711650018328], [-82.24547300313134, 38.2670555034411], [-82.24526401085313, 38.26699750096216], [-82.24505201156717, 38.26696550127659], [-82.2448430035729, 38.26696051212127], [-82.2446359024616, 38.26698450366226], [-82.2442989028059, 38.267062503878975], [-82.24396500445437, 38.26710250754337], [-82.24391210416798, 38.267116401469764]]}, 'type': 'Feature', 'properties': {'layer': 'Test', 'District': 2.0, 'Route': 1659.0, 'ROUTEID': '0601659000000', 'Label': '1659', 'BMP': 0.0, 'SuppCode': 0.0, 'EMP': 0.2726330565984828, 'ONEWAY': False, 'Shape_Leng': 438.195605355, 'SubRoute': 0.0, 'CountyCode': 6.0, 'SignSystem': 0.0, 'StreetName': 'UNKNOWN'}}, {'geometry': {'type': 'LineString', 'coordinates': [[-82.25756091240328, 38.26894600023729], [-82.25764991249889, 38.26890600170117], [-82.25784390117042, 38.26877700267332], [-82.25793290126603, 38.26873500514037], [-82.25813071418088, 38.2686837040371], [-82.25844100175891, 38.2686330075052], [-82.25868800072931, 38.26854400263696], [-82.25887290027458, 38.26846100262], [-82.25902790261898, 38.26841100925381], [-82.25927700754255, 38.26835600211572], [-82.25971201260109, 38.26829301161152], [-82.25998900306877, 38.268214009144145], [-82.26023990486283, 38.268165002728665], [-82.26031500147656, 38.26808700369591], [-82.26074190228246, 38.26748800337549], [-82.2609439009102, 38.26725400384484], [-82.26102691318374, 38.267187006266056], [-82.2612690035021, 38.26703600339289], [-82.26131000148598, 38.267003000135475], [-82.26141101389658, 38.26688600379623], [-82.26147090259474, 38.2668370005978], [-82.26174000359606, 38.26668000011614], [-82.26198990480043, 38.26650900242774], [-82.26225990161765, 38.26625800025698], [-82.26246390666347, 38.26612400320022], [-82.26263091084547, 38.266040000928854], [-82.26310390164144, 38.26589100699266], [-82.26315990323201, 38.26585300164422], [-82.26324491144624, 38.26576500520159], [-82.26333191560116, 38.26570601042482], [-82.26355490041897, 38.265651009464506], [-82.26369901152793, 38.265590007378506], [-82.26381090469658, 38.265507012212254], [-82.26397390128113, 38.26535600173338], [-82.2640820016386, 38.26528800290458], [-82.26424550113734, 38.26522350020642], [-82.26433611474931, 38.265193103876186], [-82.26436910801567, 38.26518230268732], [-82.26438510173466, 38.26516740066364], [-82.26438401208725, 38.26514930270085], [-82.2643768141279, 38.265121904844506], [-82.26434680167586, 38.26511230057926], [-82.26427671324927, 38.26510750050275], [-82.26417411351576, 38.265117001939245], [-82.2640954022063, 38.2651187006808], [-82.26405770459678, 38.26511860196456], [-82.2637970012147, 38.265088806114335]]}, 'type': 'Feature', 'properties': {'layer': 'Test', 'District': 2.0, 'SignSystem': 8.0, 'ROUTEID': '0680909000000', 'Label': '909', 'BMP': 0.0, 'SuppCode': 0.0, 'EMP': 0.506285316826147, 'ONEWAY': False, 'Shape_Leng': 814.465155147, 'SubRoute': 0.0, 'CountyCode': 6.0, 'Route': 909.0, 'StreetName': '909'}}, {'geometry': {'type': 'LineString', 'coordinates': [[-82.25734591134824, 38.2351710017293], [-82.25767050054856, 38.235489701889804], [-82.25778250372969, 38.23558420353717], [-82.25787110044621, 38.23567400591193], [-82.25796301325317, 38.23574500336707], [-82.25806791277137, 38.23580200208522], [-82.25815510028042, 38.235831505446924], [-82.25818590377457, 38.23584200238625], [-82.25834190146998, 38.23587400343419], [-82.25858111050911, 38.2359060003532], [-82.25875890115276, 38.235912008003595], [-82.25878530414775, 38.23591780991208], [-82.2589100006735, 38.23594570021464], [-82.25892890710384, 38.2359500002087], [-82.25906790001318, 38.2360100108169], [-82.25912590278313, 38.23604200356124], [-82.2591788135469, 38.23607110357321], [-82.2593623038847, 38.236212003098785], [-82.25941581185907, 38.23623691005096], [-82.25961351476144, 38.236328904810904], [-82.25962501368485, 38.23633200325921], [-82.25974491157103, 38.23634340126847], [-82.25976110436022, 38.23634500192739], [-82.26000500202645, 38.23632200428213], [-82.26018101151567, 38.2363210002695], [-82.2602970013395, 38.236330007578715], [-82.26041140384041, 38.23634900563192], [-82.26076511491556, 38.23640800366985], [-82.26094590208959, 38.23641401127878], [-82.2611507034162, 38.23641180163091], [-82.26172060472891, 38.23648911046337], [-82.26227590057533, 38.23648310697541], [-82.26232890039682, 38.23649420869569], [-82.26260760391597, 38.23655250298626], [-82.2627203038428, 38.236585404860705], [-82.26312590413727, 38.236703400505064], [-82.26321670110337, 38.23674511205945], [-82.26324610062875, 38.23675400410224], [-82.26341110363137, 38.23681500982315], [-82.2635640000226, 38.23689300950883], [-82.2636157006491, 38.23695060396881], [-82.26367610273883, 38.23701800798659], [-82.26380810199771, 38.23719200890048], [-82.26388230279554, 38.237260108087696], [-82.26393210177775, 38.237294902427266], [-82.26399490318727, 38.23733500477576], [-82.26436191529501, 38.23750800093487], [-82.26450791233219, 38.23760800135733], [-82.26458280463703, 38.23768600019241], [-82.2646259033354, 38.237731011193375], [-82.26467310392763, 38.237797402266125], [-82.26477391202934, 38.23795800381032], [-82.26502910431009, 38.23818470357489], [-82.26515960006509, 38.23832760286001], [-82.26515990390908, 38.23832800198514], [-82.26522290438879, 38.23843800408204], [-82.26529141073115, 38.238594110984025], [-82.26529800100252, 38.238609001998924], [-82.26537070353515, 38.238855211465136], [-82.2654170030728, 38.239012000503834], [-82.26543720345944, 38.239069309374486], [-82.265625, 38.23963660221446]]}, 'type': 'Feature', 'properties': {'layer': 'Test', 'District': 2.0, 'SignSystem': 4.0, 'Label': '43', 'ROUTEID': '0640043000000', 'BMP': 0.0, 'SuppCode': 0.0, 'EMP': 0.6029011336533829, 'ONEWAY': False, 'Shape_Leng': 10098.2225671, 'SubRoute': 0.0, 'CountyCode': 6.0, 'Route': 43.0, 'StreetName': 'RACCOON CREEK RD'}}]
'''
```
