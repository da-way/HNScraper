import requests as req
from bs4 import BeautifulSoup as bs


def data_fetch(base, page):
    url = base + '?p=' + page
    res = req.get(url)
    soup = bs(res.text, 'html.parser')
    links_parent = soup.select('.storylink')
    points_parent = soup.select('.subtext')
    print(create_custom_hn(links_parent, points_parent))


def manipulation(nl):
    sort_list = sorted(nl, key=lambda k: int(k['points'][:k['points'].index(" ")]), reverse=True)
    filter_list = list(filter(lambda f: int(f['points'][:f['points'].index(" ")]) > 100, sort_list))
    return filter_list


def points_list(pl):
    new_pl = []
    for p in pl:
        ws_pos = p.text.index(" ")
        ele = p.text[1:ws_pos] + ' points' if p.find('span', class_="score") else '0 points'
        new_pl.append(ele)
    return new_pl


def create_custom_hn(lp,pp):
    custom_hn = []
    new_points_list = points_list(pp)
    titles = [t.text for t in lp]
    links = [l.get('href') for l in lp]
    for idx, item in enumerate(titles):
        something = {
            "title": titles[idx],
            "link": links[idx],
            "points": new_points_list[idx]
        }
        custom_hn.append(something)
    return manipulation(custom_hn)


data_fetch('https://news.ycombinator.com/news', "1")



