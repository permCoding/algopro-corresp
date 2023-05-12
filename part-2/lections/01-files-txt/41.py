import requests as req
from bs4 import BeautifulSoup as bs  # pip install bs4


def get_html(url):
    html = req.get(url)
    html.encoding = 'utf8'
    return html.text


url = 'https://www.sports.ru/rfpl/table/'
html = get_html(url)
soup = bs(html, 'html.parser')  # 'lxml'

# table = soup.find('table', { 'class': 'stat-table' } )  # class="stat-table table sortable-table"
table = soup.find('table', class_='stat-table')
print(table)
