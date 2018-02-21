from django.db import models

# Create your models here.
# DATABASE SCHEMA HERE
# THINK OF TABLES/RELATIONS


class Notification_Payload(models.Model):

    header = models.CharField(max_length=250)
    content = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=250)

    def __init__(self,header,content,image_url):
        self.header = header
        self.content = content
        self.image_url = image_url

    # series of getter functions

    def GetHeader(self):
        return self.header

    def GetContent(self):
        return self.content

    def GetImage_Url(self):
        return self.image_url

class Notification(models.Model,Notification_Payload):

    to_be_sended_on = models.DateTimeField()
    def __init__(self, header, content, image_url,to_be_sended_on):
        Notification_Payload.__init__(self,header,content,image_url)
        self.to_be_sended_on = to_be_sended_on

    def GetTo_be_sended_on(self):
        return self.to_be_sended_on