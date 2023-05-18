from bs4 import BeautifulSoup as bs  # pip install bs4
from module import get_html, to_json


def get_records(html):
    soup = bs(html, 'html.parser')
    posts = soup.find_all('div', class_="prod__post")
    records = []
    for post in posts:
        record = {
                'title': post.find('div', class_="post__title").text.strip(), 
                'text': post.find('div', class_="post__text").text.strip()
            }
        records.append( record )
    return records


url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)
records = get_records(html)
to_json('results.json', records, ';')
