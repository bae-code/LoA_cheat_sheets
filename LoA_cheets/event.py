from django.forms import DateInput
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for a in range(2):
    page = a + 1
    data = requests.get(f'https://lostark.game.onstove.com/News/Event/Now?page={page}&searchtype=0&searchtext=',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    event = soup.select('#lostark-wrapper > div > main > div > div > div.list.list--event > ul > li')

    event_list = []
    a = ''
    for e in event:
        title= e.select_one('a > div.list__thumb > img')['alt']
        image = e.select_one('a > div.list__thumb > img')['src']
        date = e.select_one('a > div.list__term').text.split(':')[1]
        a =title,image,date
        event_list.append(a) 


print(event_list)