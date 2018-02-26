from django.contrib import admin
from .models import User,Notification
# Register your models here.
# admin section of this app
# delete user and delete post
# more to be added

admin.site.register(User)
admin.site.register(Notification)