from django.http import HttpResponse
# Create your views here.
# THESE ARE PYTHON FUNCTIONS
# WHICH RESPOND TO USER REQUEST
# and responses are like logout and html


def index(request):
    return HttpResponse("<h1>uptil video 5 new boston")