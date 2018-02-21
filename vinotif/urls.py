from django.conf.urls import include, url
from django.contrib import admin

#USER REQUESTS FIRST ARRIVE HERE

urlpatterns = [
    # Examples:
    # url(r'^$', 'vinotif.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(matching pattern,response_to_user )
    # match the longest/shortest)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scheduler/', include('scheduler.urls')),
    # remove cluttering from here
    # apps urls must go to there own apps
    # be organized<just some dev. shit>
]
