from django.core.mail import send_mail
from t4c.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from digital.models import emailCampaign
from smtplib import SMTPException


def send_campaign_email():
    obj_ids = emailCampaign.objects.filter(subscribe=True,sent_message=False).values_list('pk', flat=True)[:20]
    obj = emailCampaign.objects.filter(pk__in=list(obj_ids))
    subject = "Launch Offer"
    sender = "info@t4cdigital.com"
    # receivers = [item.email for item in obj]
    for recipient in obj:
        msg_html = render_to_string('digital/campaign_template.html', {'name': recipient.name})
        try:
            #I used EmailMultiAlternatives because I wanted to send both text and html
            emailMessage = EmailMultiAlternatives(subject=subject,from_email=sender, to=[recipient.email,], reply_to=[sender,])
            emailMessage.attach_alternative(msg_html, "text/html")
            emailMessage.send(fail_silently=False)
            emailCampaign.objects.filter(pk__in=list(obj_ids)).update(sent_message=True)
        except SMTPException as e:
            print('There was an error sending an email: ', e) 
            error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
            raise serializers.ValidationError(error)


def send_mail_to(subject, message, receivers):   
    send_mail(subject,message,EMAIL_HOST_USER,[receivers],   fail_silently= False)




