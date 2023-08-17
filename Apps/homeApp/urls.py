from django.contrib import admin
from django.urls import path,include
from .views import base,delete_data,upload_data,predict_csv_single,predict_csv_multi,predict_data_manually,view_data,retrieve_data_by_id,analysis,change_password,login2,account_details,add_files_multi,about,dashboard,userLogout,reports,upload_credit_data,prediction_button,enter_form_data_manually,add_files_single

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('about/',about,name='about'),
    path('dashboard/',dashboard,name='dashboard'),
    path('reports/',reports,name='reports'),
    path('upload_credit_data/',upload_credit_data,name='upload_credit_data'),
    path('prediction_button/<int:id>',prediction_button,name='prediction_button'),
    
    #for main adminstrator upload 
    
    path('upload_data/',upload_data,name='upload_data'),
    path('delete_data/<int:id>/',delete_data,name='delete_data'),


    path('enter_form_data_manually/',enter_form_data_manually,name='enter_form_data_manually'),
    path('add_files_single/<int:id>',add_files_single,name='add_files_single'),
    path('add_files_multi/<int:id>',add_files_multi,name='add_files_multi'),

    path('predict_data_manually/',predict_data_manually,name='predict_data_manually'),
    path('predict_csv_single/<int:id>',predict_csv_single,name='predict_csv_single'),
    path('predict_csv_multi/<int:id>',predict_csv_multi,name='predict_csv_multi'),

    path('account_details/',account_details,name='account_details'),
    path('change_password/',change_password,name='change_password'),
    path('analysis/<int:id>/',analysis,name='analysis'),
    path('view_data/<int:id>',view_data,name='view_data'),
    path('retrieve_data_by_id/<int:id>/',retrieve_data_by_id,name='retrieve_data_by_id'),
]
