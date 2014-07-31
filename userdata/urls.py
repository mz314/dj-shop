from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from userdata.views import *


urlpatterns = patterns('',
    url(r'^create/$',create_user),

)


