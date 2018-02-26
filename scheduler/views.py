from django.http import HttpResponse
from .models import *


# Create your views here.
# THESE ARE PYTHON FUNCTIONS
# WHICH RESPOND TO USER REQUEST
# and responses are like logout and html


def index(request):
    return HttpResponse("<h1>uptil video 5 new boston</h1>")


def users(request):
    str = ""

    for record in User:
        str = str + record + '<br>'

    return HttpResponse(str)


def notifs(request):
    str = ""

    for record in Notification:
        str = str + record + '<br>'

    return HttpResponse(str)
