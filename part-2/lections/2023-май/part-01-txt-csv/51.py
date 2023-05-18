import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    html = req.get(url, headers=ua)
    html.encoding = 'utf8'  # коммент
    return html.text


def print_rows():
    soup = bs(html, 'html.parser')  # 'lxml'

    trs = soup \
        .find('table', class_='stat-table') \
        .find('tbody') \
        .find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        print(tds[0].text, tds[1].text, tds[8].text)


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
print_rows()
