from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from userdata.views import *
from userdata.rest_views import *


urlpatterns = patterns('',
    url(r'^create/$',create_user),
    url(r'get/check',LoginCheckView.as_view()),
    url(r'get',UserDataView.as_view()),
)


