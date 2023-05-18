from django.db import models
#from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class Pricing(models.Model):
    name_of_service = models.CharField(max_length=200,default='')
    first_package = models.PositiveSmallIntegerField(default=0)
    second_package = models.PositiveSmallIntegerField(default=0)
    third_package = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name_of_service


class PaypalClient(models.Model):
    name_of_env = models.CharField(max_length=200,default='',unique=True)
    client_id = models.TextField()

    def __str__(self):
        return self.name_of_env



class emailCampaign(models.Model):
    subject = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=50,default='')
    name = models.CharField(max_length=50,default='')
    subscribe = models.BooleanField(default=False)
    sent_message = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class customPrice(models.Model):
    logo_flyer = models.PositiveSmallIntegerField(default=0)
    frontend = models.PositiveSmallIntegerField(default=0)
    backend = models.PositiveSmallIntegerField(default=0)
    devops = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "Customised Package {}".format(self.logo_flyer)


class emailFile(models.Model):
    filename = models.CharField(max_length=100,default='')
    file = models.FileField(upload_to='emailfile/',blank=True,max_length=1000)

    def __str__(self):
        return "Email campaign {}".format(self.filename)
