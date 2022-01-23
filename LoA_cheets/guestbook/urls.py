# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.load_guestbook, name= 'guestbook'),

]