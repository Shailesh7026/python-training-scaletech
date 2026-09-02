import requests as req

url = "https://fakestoreapi.com/products"

#GET
res = req.get(url)

# print(res.status_code)
# # print(res.content)
# print(res.json())


new_product = {
  "id": 123,
  "title": "Samsung S21 Ultra",
  "price": 10000,
  "description": "desc",
  "category": "Electronics",
  "image": "http://example.com"
}

#POST
res = req.post(url, json=new_product)
print(res.status_code)
# print(res.content)
print(res.json())


product_id = 1
patch_data = {
  "price": 1,
  "title": "Samsung S21 Ultra"
}

#PATCH
try:
    res = req.patch(f"{url}/{product_id}", json=patch_data)
    print(res.status_code)
    print(res.json())
except Exception as e:
    print(f"Error: {e}")


# Delete
try:
    res = req.delete(f"{url}/{product_id}")
    print(res.status_code)
    print(res.json())
except Exception as e:
    print(f"Error: {e}")






