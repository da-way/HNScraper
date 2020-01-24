import requests as req
from bs4 import BeautifulSoup as bs

# Setup
res = req.get('https://news.ycombinator.com/news')
soup = bs(res.text, 'html.parser')
links = soup.select('.storylink')
st = soup.select('.subtext')
for s in st:
    ws = s.text.index(" ")
    new = int(s.text[1:ws]) if s.find('span', class_="score") else "NONE"
    print(new)
    # new.append(s.text[1:ws] if s.get_text())

# print(f'Links has {len(links)} & Subtext has {len(st)}')
# print(new)