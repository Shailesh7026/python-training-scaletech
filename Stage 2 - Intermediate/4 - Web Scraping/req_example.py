import requests as req

url = "https://fakestoreapi.com/products"

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

res = req.post(url,new_product)
print(res.status_code)
# print(res.content)
print(res.json())






