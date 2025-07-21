import requests
from bs4 import BeautifulSoup
import pandas as pd

print("✅ Starting web scraping...")

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

titles = []
prices = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    titles.append(title)
    prices.append(price)

df = pd.DataFrame({'Title': titles, 'Price': prices})
df.to_csv('books.csv', index=False)

print("✅ Scraping complete! Data saved to books.csv")
