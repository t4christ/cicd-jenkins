from django.urls import path

from digital.views import home,terms,privacy,contactus,sendEmailCampaign,emailList

app_name = 'digital'
urlpatterns =[
    path('',home, name='home'),
    path('contact',contactus, name='contactus'),
    path('email',sendEmailCampaign, name='email_template'),
    path('emailupload',emailList, name='upload'),
    path('terms',terms, name='terms'),
    path('privacy',privacy, name='privacy'),
]
