from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from userdata.views import *
from userdata.form_views import *

urlpatterns = patterns('',
                       url(r'^create/$', create_user),
                       url(r'^logout/$', logout_user,name='logout'),
                       url(r'^login$', login_user,name='login'),
                       url(r'^login_http$', login_user_http,name='login_user'),

)
