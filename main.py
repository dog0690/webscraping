from bs4 import BeautifulSoup
import requests

url = ('https://finance.yahoo.com/markets/crypto/active/')
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("tbody", class_ = "body yf-paf8n5")
