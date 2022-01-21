# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('raid/', views.call_raid, name='raid'),
    path('valtan/', views.call_raid, name='valtan'),
]