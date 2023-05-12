import requests as req

url = 'https://www.sports.ru/rfpl/table/'
html = req.get(url)
html.encoding = 'utf8'

f = open('sports.html', 'w', encoding='utf8')
f.write(html.text)
f.close()
