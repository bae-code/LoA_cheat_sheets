# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('valtan/', views.call_valtan, name='valtan'),
    path('Biackiss/', views.call_bia, name='Biackiss'),
    path('Kouku/', views.call_kouku, name='Kouku'),
    path('Abrelshud/', views.call_abrel, name='Abrelshud'),
    path('test/', views.test, name='test'),
]