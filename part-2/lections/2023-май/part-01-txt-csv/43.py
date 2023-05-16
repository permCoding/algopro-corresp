import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    html = req.get(url)
    html.encoding = 'utf8'
    return html.text


def get_records(html):
    soup = bs(html, 'html.parser')  # 'lxml'

    trs = soup \
        .find('table', class_='stat-table') \
        .find('tbody') \
        .find_all('tr')
    
    records = []
    for tr in trs:
        tds = tr.find_all('td')
        record = [int(tds[0].text), tds[1].text, int(tds[6].text), int(tds[8].text)]
        records.append( record )
    
    return records


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
records = get_records(html)
for rec in sorted(records, key=lambda x: x[2], reverse=True):
    print(rec)
