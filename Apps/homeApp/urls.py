from django.contrib import admin
from django.urls import path,include
from .views import base,login2,about,dashboard,userLogout,reports

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('about/',about,name='about'),
    path('dashboard/',dashboard,name='dashboard'),
    path('reports/',reports,name='reports')
]
