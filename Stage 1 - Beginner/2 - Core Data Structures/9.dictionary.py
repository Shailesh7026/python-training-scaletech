dic = {
    "name": "Shailesh",
    "age": 20
}

print(dic["name"]) # Shailesh ⚠️ This will throw KeyError if key is not present in dictionary
print(dic.get("name" , "Key not found")) # Shailesh ✅ This will return "Key not found" if key is not present in dictionary

# Dictionary methods
dic["name"] = "Shailesh Kumar"
dic["id"] = "23X1"
print(dic) # {'name': 'Shailesh Kumar', 'age': 20, 'id': '23X1'}

print(dic.keys()) # dict_keys(['name', 'age', 'id'])
print(dic.values()) # dict_values(['Shailesh Kumar', 20, '23X1'])
print(dic.items()) # dict_items([('name', 'Shailesh Kumar'), ('age', 20), ('id', '23X1')])


# dictionary comprehension
fruits = { "apple": 2.00 , "orange":3.00 , "banana": 2.3 }
double_price_fruits = {fruit: price * 2 for fruit,price in fruits.items()}

print(double_price_fruits)


        
