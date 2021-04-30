"""extracts data from the data.json file"""
import json
with open('data.json') as file:
    json_obj = json.load(file)
    data = {}
    for key, value in json_obj.items():
        data[key] = value['email'], value['password']
    print(data)
