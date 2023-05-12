import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.sports.ru/rfpl/table/'
resp = requests.get(url)
resp.encoding = "utf8"
html = resp.text

soup = bs(html, 'html.parser')

trs = soup \
    .find('table', class_="stat-table") \
    .find('tbody') \
    .find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    print(tds[0].text, tds[1].text, tds[3].text)


'''
https://www.championat.com/football/_england/tournament/4013/table/  
https://www.championat.com/hockey/_superleague/tournament/5077/table/  
https://www.soccer.ru/main/table
https://www.sports.ru/rfpl/table/
'''