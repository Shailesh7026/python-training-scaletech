import requests
import json 

res = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(res.text)

print(json.dumps(data[0],indent=4,sort_keys=True))