from django.contrib import admin
from django.urls import path,include
from .views import base,login2,about,home,userLogout

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('about/',about,name='about'),
    path('home_page/',home,name='home')
]
