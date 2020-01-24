import requests as req
from bs4 import BeautifulSoup as bs

# Setup
res = req.get('https://news.ycombinator.com/')
soup = bs(res.text, 'html.parser')
# links = soup.select('.storylink')
# {title: "", link:"", score:" points"}  --
# final = [l.getText() for l in links]
# print()
def create_custom_hn(soup):
    pass

