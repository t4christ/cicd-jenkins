#import the task from celery

from celery.utils.log import get_task_logger
from celery import shared_task 
from t4c.settings import EMAIL_RECEIVER

from time import sleep
from .mail import send_mail_to,send_campaign_email 


logger = get_task_logger(__name__)

print("Inside celery")
     
@shared_task(name='contactus_task')
def contactus_task(subject,message,receiver):
   print("Am in here for a start celery")
   is_task_completed= False   
   error=''   
   try:       
      sleep(5)       
      is_task_completed= True   
   except Exception as err:       
      error= str(err)       
      logger.error(error)   
   if is_task_completed:       
       send_mail_to(subject,message,receiver)
       print("Sent")
   else:
        print(error)       
    #   send_mail_to(subject,error,receiver)   
        return('contactus_task_done')


@shared_task(name='sendcampaign_task')
def sendcampaign_task():
   print("Am in here for a start celery")
   is_task_completed= False   
   error=''   
   try:       
      sleep(5)       
      is_task_completed= True   
   except Exception as err:       
      error= str(err)       
      logger.error(error)   
   if is_task_completed:       
       send_campaign_email() 
       print("Sent")
   else:
        print(error)       
    #   send_mail_to(subject,error,receiver)   
        return('campaignemail_done')