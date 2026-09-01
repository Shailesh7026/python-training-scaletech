import requests as req

def get_user_data():
    res = req.get("https://api.github.com/users/shailesh7026")
    return res.json()
