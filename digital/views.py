from django.shortcuts import render,redirect
from django.contrib import messages
from t4c.settings import EMAIL_HOST_USER,EMAIL_RECEIVER
from .tasks import contactus_task,sendcampaign_task
from .models import PaypalClient, Pricing, customPrice, emailFile,emailCampaign
import urllib.request
import wget
from django.core.mail import send_mail
import csv   
import os

def home(req):
    template = "digital/home.html"
    obj = Pricing.objects.all()
    customised_package =  customPrice.objects.all()
    paypal_client = PaypalClient.objects.get(name_of_env='sandbox')
    context = {"pricing":obj,"env":paypal_client,"customer":customised_package}
    return render(req,template,context)


def sendEmailCampaign(req):
    try:
        sendcampaign_task.delay()
        messages.success(req, "Email Campaign Sent Out")
    except:
        messages.error(req,"There was an error sending out mail")
    return redirect("/")


def emailList(request):
    emailfile = emailFile.objects.all()[0]
    path = "email.csv"
    filename = os.path.exists(path)
    if filename:
        os.remove(path)
    wget.download(emailfile.file.url,out="email.csv")
    try:
        print("Am in reader",)
        emailCampaign.objects.all().delete()
        with open("email.csv") as csvfile:
            reader = csv.DictReader(csvfile,delimiter=',')
            next(reader) 
            get_details = None
            for row in reader:
                client_name = row['client_name']
                client_email = row['client_email']
                get_details = emailCampaign(name=client_name,email=client_email,subscribe=True)
                get_details.save()
        messages.success(request, "Email Campaign File Updated")

    except Exception as e:
            print(e)
            messages.error(request,"There was an error uploading your mail file.")
    return redirect("/")



def contactus(request):
    print("Am here for a start")
    full_name = request.POST.get('name')
    email = request.POST.get('email')
    sub = request.POST.get('subject')
    message = request.POST.get('message')
    subject = None
    msg = None
    notify = None
    if request.POST.get('sub_email'):
        email = request.POST.get('sub_email')
        subject = "CLIENT NEWSLETTER"
        notify = "You have successfully subscribed for our newsletter"
        msg ="Hi Admin, user with email address {} just subscribed to your newsletter".format(email)

    else:
        subject = "CLIENT INFO"
        notify = "Your Message has been sent. We will get back to you shortly"
        msg = "Hi Admin, {} with the email address {} and subject of concern {} sent you this message {}".format(full_name,email,sub,message)

        
    receiver = EMAIL_RECEIVER
    # send_mail(subject,message,EMAIL_HOST_USER,[receiver], fail_silently= False)

    print("Am in the middle",full_name,email,sub,msg)
    contactus_task.delay(subject,msg,receiver)
    print("AM here")
    messages.success(request, notify)
    return redirect("/")


def terms(req):
    template = "digital/terms.html"
    return render(req,template)

def privacy(req):
    template = "digital/privacy.html"
    return render(req,template)
