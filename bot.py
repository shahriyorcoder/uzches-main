import requests
from bs4 import BeautifulSoup 

r = requests.get('https://stadion.uz/') 
#   id="standings_table"
soup = BeautifulSoup(r.content, 'html.parser') 



# s = soup.find(id='standings_place').find(id="standings_table")
# # content = s.find_all('tbody') 
# rows = s.find_all("tr")
# for x in rows:
#     # for t in x:
#     for c in  x.find_all('td'):
#         print(c.text)

s = soup.find(id='online_tablo').find('ul')

for x in s.find_all('li'):
    for t in x.find_all('ul'):
        print(t)


