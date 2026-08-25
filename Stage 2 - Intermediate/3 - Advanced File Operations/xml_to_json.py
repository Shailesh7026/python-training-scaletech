import xmltodict
import json


with open("data.xml") as file:
    data_dict = xmltodict.parse(file.read())
    
    json_data = json.dumps(data_dict)
    
    print(json_data)

