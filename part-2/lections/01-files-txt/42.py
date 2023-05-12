import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    html = req.get(url)
    html.encoding = 'utf8'
    return html.text


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
soup = bs(html, 'html.parser')  # 'lxml'

trs = soup \
    .find('table', class_='stat-table') \
    .find('tbody') \
    .find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    print(tds[0].text, tds[1].text, tds[8].text)
