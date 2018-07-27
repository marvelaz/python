import json, mpu

with open('sedona_config2.json') as json_file:
    data = json.load(json_file)


lat1 = 22.88328708
lon1 = -102.29083059
distance = {}

km = 60
max_distance =[]

total = []

for p in data['sites']:
    if p['group'] == True:
        continue
    else:
        lat2 = p['latitude']
        lon2 = p['longitude']
        d = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
        max_distance.append(d)
        distance.setdefault('Router1', {})['Lat'] = lat2
        distance.setdefault('Router1', {})['Long'] = lon2
        if d <= 355:#km:
            name = p['name']
            distance.setdefault('Router1', {}).setdefault('nearby sites', {})[name] = d

        distance.setdefault('Router1', [])['Min_distance'] = min(max_distance)

distance.setdefault('Router1', [])['Nearest site'] = min(distance['Router1']['nearby sites'], key=distance['Router1']['nearby sites'].get)
distance.setdefault('Router1', [])['Farther site'] = max(distance['Router1']['nearby sites'], key=distance['Router1']['nearby sites'].get)

print(json.dumps(distance, indent=4))

