from django.shortcuts import render
from django.http.response import HttpResponseRedirect,HttpResponse

def base(request):
    return render(request,'homeApp/base.html')