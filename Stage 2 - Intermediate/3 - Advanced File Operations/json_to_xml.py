import xml.etree.ElementTree as ET
import json


json_str = '{"name" : "Shailesh","Age" : 11}'

data = json.loads(json_str)

root = ET.Element("data")

for key,value in data.items():
    ET.SubElement(root,key).text = str(value)
    
tree = ET.ElementTree(root)

print(tree)

tree.write("data.xml")

## Another Easy Way 

# import json
# import xmltodict

# json_str = '{"name" : "Shailesh","Age" : 11}'
# data_dict = json.loads(json_str)

# # Convert dictionary back into an XML string document
# xml_string = xmltodict.unparse(data_dict, pretty=True)
# print(xml_string)

