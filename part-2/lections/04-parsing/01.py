import requests

url = 'https://www.sports.ru/rfpl/table/'
resp = requests.get(url)
resp.encoding = "utf8"
html = resp.text

print(html)

'''
https://www.championat.com/football/_england/tournament/4013/table/  
https://www.championat.com/hockey/_superleague/tournament/5077/table/  
https://www.soccer.ru/main/table
https://www.sports.ru/rfpl/table/
'''