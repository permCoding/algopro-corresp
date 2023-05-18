from bs4 import BeautifulSoup as bs  # pip install bs4
import module


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
html = module.get_html(url)
records = get_records()
for rec in records: print(*rec)
