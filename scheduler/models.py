from django.db import models


# Create your models here.
# DATABASE SCHEMA HERE
# THINK OF TABLES/RELATIONS


class Notification_Payload(models.Model):
    header = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=250)

    class Meta:
        abstract = True


class Notification(Notification_Payload):
    to_be_sended_on = models.DateTimeField()

class User(models.Model):
    name = models.CharField(max_length=250)
    mailid = models.CharField(max_length = 250)