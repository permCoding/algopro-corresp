from bs4 import BeautifulSoup as bs  # pip install bs4
from module import get_html
import json


def get_records(html):
    soup = bs(html, 'html.parser')

    trs = soup \
        .find('table', class_='stat-table') \
        .find('tbody') \
        .find_all('tr')
    records = []
    for tr in trs:
        tds = tr.find_all('td')
        record = {
                'id': int(tds[0].text), 
                'team': tds[1].text, 
                'ball_up': int(tds[6].text), 
                'ball_down': int(tds[8].text)
            }
        records.append( record )
    return records


def to_json(filename, records, sep=','):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(records, f, indent=4, ensure_ascii=False)


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
records = get_records(html)
to_json('results.json', records, ';')
