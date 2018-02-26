from django.db import models


# Create your models here.
# DATABASE SCHEMA HERE
# THINK OF TABLES/RELATIONS
# DO TABLES HAVE METHODS ? NO
# Hence no __init__ method here


class User(models.Model):
    name = models.CharField(max_length=250)
    mailid = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Notification_Payload(models.Model):
    header = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    class Meta:
        abstract = True


class Notification(Notification_Payload):
    to_be_sended_on = models.DateTimeField()

    def __str__(self):
        return self.header
