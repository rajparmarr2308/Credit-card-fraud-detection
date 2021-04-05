from django.shortcuts import render
from django.http.response import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import authenticate, login, logout

def base(request):
    return render(request,'homeApp/landing_page.html')
    
def upload_credit_data(request):
    return render(request,'homeApp/upload_credit_data.html')
def prediction_button(request):
    return render(request,'homeApp/fraud_detection.html')
    
def reports(request):
    return render(request,'homeApp/reports.html')
    
def enter_form_data_manually(request):
    return render(request,'homeApp/enter_form_data_manually.html')
def add_files_single(request):
    return render(request,'homeApp/add_files_single.html')
def add_files_multi(request):
    return render(request,'homeApp/add_files_multi.html')
def account_details(request):
    return render(request,'homeApp/account_details.html')
def change_password(request):
    return render(request,'homeApp/change_password.html')
def analysis(request):
    return render(request,'homeApp/analysis.html')
def view_data(request):
    return render(request,'homeApp/view_data.html')

def userLogout(request):
    try:
      del request.session['username']
    except:
      pass
    logout(request)
    return HttpResponseRedirect('/') 
    

def login2(request):
    data = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        
        else:    
            data['error'] = "Username or Password is incorrect"
            res = render(request, 'homeApp/login.html', data)
            return res
    else:
        return render(request, 'homeApp/login.html', data)


def about(request):
    return render(request,'homeApp/about.html')

def dashboard(request):
    return render(request,'homeApp/dashboard.html')