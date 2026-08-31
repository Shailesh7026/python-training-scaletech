import requests as req
from bs4 import BeautifulSoup

# Let's Parse some Movies to watch 
# url = "https://www.rottentomatoes.com/"

# res = req.get(url)
# soup = BeautifulSoup(res.content,"html.parser")

# content = soup.find('rt-text')

# if content:
#     print(content)
# else:
#     print("No data")


url = "https://www.passiton.com/inspirational-quotes"
response = req.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = []
quote_boxes = soup.find_all('div', class_='grid grid-cols-2 lg:grid-cols-4 gap-8')
for box in quote_boxes:
    quote_text = box.img['alt'].split(" #")
    quote = {
        'theme': box.h5.text.strip(),
        'image_url': box.img['src'],
        'lines': quote_text[0],
        'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
    }
    quotes.append(quote)
# Display extracted quotes
for q in quotes[:5]:  # print only first 5 for brevity
    print(q)
