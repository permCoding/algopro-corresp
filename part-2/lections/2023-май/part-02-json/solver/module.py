import requests as req
import json


def get_html(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    html = req.get(url, headers=ua)
    html.encoding = 'utf8'  # коммент
    return html.text


def to_json(filename, records, sep=','):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(records, f, indent=4, ensure_ascii=False)
