import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def main_view(request):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    event_list = []
    for a in range(2):
        page = a + 1
        data = requests.get(f'https://lostark.game.onstove.com/News/Event/Now?page={page}&searchtype=0&searchtext=',headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        event = soup.select('#lostark-wrapper > div > main > div > div > div.list.list--event > ul > li')

        
        for e in event:
            title= e.select_one('a > div.list__thumb > img')['alt']
            image = e.select_one('a > div.list__thumb > img')['src']
            date = e.select_one('a > div.list__term').text.split(':')[1]
            a = title,image,date
            event_list.append(a)
    return render(request, 'main.html',{'events': event_list})

def call_valtan(request):
    if request.method =="GET":
        return render(request,'detail/Valtan.html')

def call_bia(request):
    if request.method =="GET":
        return render(request,'detail/Biackiss.html')

def call_kouku(request):
    if request.method =="GET":
        return render(request,'detail/Kouku.html')

def call_abrel(request):
    if request.method =="GET":
        return render(request,'detail/Abrelshud.html')

        
def test(request):
    jsonObject = json.loads(request.body)
    a = jsonObject.get('title')
    print(a[0:2])

    return JsonResponse(jsonObject)

