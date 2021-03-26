from django.shortcuts import render
from django.http.response import HttpResponseRedirect,HttpResponse

def base(request):
    return render(request,'homeApp/landing_page.html')


def login(request):
    return render(request,'homeApp/login.html')

def about(request):
    return render(request,'homeApp/about.html')