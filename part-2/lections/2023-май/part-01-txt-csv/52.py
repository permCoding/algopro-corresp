import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    html = req.get(url, headers=ua)
    html.encoding = 'utf8'  # коммент
    return html.text


def get_records():
    soup = bs(html, 'html.parser')  # 'lxml'

    trs = soup \
        .find('table', class_='stat-table') \
        .find('tbody') \
        .find_all('tr')

    records = []
    for tr in trs:
        tds = tr.find_all('td')
        record = [int(tds[0].text), tds[1].text, int(tds[8].text)]
        records.append(record)
    return records


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
records = get_records()
for rec in records: print(*rec)
