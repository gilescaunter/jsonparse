import json

f = open('stationData.txt','rU')

json_data = json.load(f)

print json_data

print json_data['data']['stations']


for station in json_data['data']['stations']:
    print station['name']




