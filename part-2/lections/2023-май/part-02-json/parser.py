import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    ua = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"    
    }
    html = req.get(url, headers=ua)
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


def to_csv(filename, records, sep=','):
    f = open(filename, 'w', encoding='utf8')
    f.write(f'id{sep}team{sep}ball{sep}\n')
    for rec in records:
        f.write(f'{rec[0]}{sep}{rec[1]}{sep}{rec[2]}\n')
    f.close()


url = 'https://www.sports.ru/rfpl/table/'

html = get_html(url)
records = get_records(html)
to_csv('./results.csv', records, ';')  # тут переделать в json
