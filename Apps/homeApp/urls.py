from django.contrib import admin
from django.urls import path,include
from .views import base,view_data,analysis,change_password,login2,account_details,add_files_multi,about,dashboard,userLogout,reports,upload_credit_data,prediction_button,enter_form_data_manually,add_files_single

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('about/',about,name='about'),
    path('dashboard/',dashboard,name='dashboard'),
    path('reports/',reports,name='reports'),
    path('upload_credit_data/',upload_credit_data,name='upload_credit_data'),
    path('prediction_button/',prediction_button,name='prediction_button'),
    path('enter_form_data_manually/',enter_form_data_manually,name='enter_form_data_manually'),
    path('add_files_single/',add_files_single,name='add_files_single'),
    path('add_files_multi/',add_files_multi,name='add_files_multi'),
    path('account_details/',account_details,name='account_details'),
    path('change_password/',change_password,name='change_password'),
    path('analysis/',analysis,name='analysis'),
    path('view_data/',view_data,name='view_data'),
]
