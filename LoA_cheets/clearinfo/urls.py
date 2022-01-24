from django.urls import path
from . import views

urlpatterns = [
    path('clearinfo/', views.clearinfo, name='clearinfo'),
]