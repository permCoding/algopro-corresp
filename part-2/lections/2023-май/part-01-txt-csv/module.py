import requests as req


def get_html(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    html = req.get(url, headers=ua)
    html.encoding = 'utf8'  # коммент
    return html.text
