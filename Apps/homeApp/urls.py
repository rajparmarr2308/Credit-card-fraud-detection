from django.contrib import admin
from django.urls import path,include
from .views import base,login,about

urlpatterns = [
    path('',base),
    path('login/',login,name='login'),
    path('about/',about,name='about'),
]
