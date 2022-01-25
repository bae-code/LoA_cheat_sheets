import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import GuestbookModel
import re
# Create your views here.
def load_guestbook(request):
    if request.method == "GET":
        all_comment = GuestbookModel.objects.all().order_by('-created_date')
        print(all_comment)
        return render(request,'guestbook/guestbook.html',{'comments': all_comment})
    elif request.method =="POST":
        content = request.POST.get('content','')
        author = request.POST.get('author')
        badwords_list = open('guestbook/badwords.txt', 'r',encoding = "utf-8")
        badwords = badwords_list.readlines()

        for i in badwords: 

            if content.find(i.strip()) >= 0 or content.isalnum():
                content = '금지어'
                break
        if content == "":
            all_comment = GuestbookModel.objects.all().order_by('-created_date')
            return render(request, 'guestbook/guestbook.html',{'error':'내용을 입력해주세요','comments': all_comment})
        else:
            if content =="금지어":
                all_comment = GuestbookModel.objects.all().order_by('-created_date')
                return render(request, 'guestbook/guestbook.html',{'error':'금지어 혹은 특수문자를 입력하셨습니다','comments': all_comment})
            else:
                author = author
                my_comment = GuestbookModel.objects.create(author=author, content=content)

                my_comment.save()
                return redirect('/guestbook')
            