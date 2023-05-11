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

lst = []
for tr in trs:
    tds = tr.find_all('td')
    lst.append([tds[0].text,tds[1].text,tds[6].text])

lst.sort(key=lambda elm: elm[2], reverse=True)
f = open('goals.csv','w',encoding='utf8')
f.write(f'id,team,goals\n')
for e in lst:
    f.write(f'{e[0]},{e[1]},{e[2]}\n')

'''
https://www.championat.com/football/_england/tournament/4013/table/  
https://www.championat.com/hockey/_superleague/tournament/5077/table/  
https://www.soccer.ru/main/table
https://www.sports.ru/rfpl/table/
'''