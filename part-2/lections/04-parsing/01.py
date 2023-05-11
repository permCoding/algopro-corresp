import requests

url = 'https://www.sports.ru/rfpl/table/'
resp = requests.get(url)
resp.encoding = "utf8"
html = resp.text

print(html)
