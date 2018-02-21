from django.conf.urls import include, url
#url() and include() functions

#make the scope of the views functions here . how ?
from . import views

#USER REQUESTS FIRST ARRIVE HERE

urlpatterns = [
    # Examples:
    # url(r'^$', 'vinotif.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # format url(matching pattern,response_to_user )
    url(r'^$',views.index,name = 'index'),
    # this matches blank URL
    # this matches scheduler immediately after url
]
