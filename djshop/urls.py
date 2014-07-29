from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
import cms.views
import djshop.ajax_urls

urlpatterns = patterns('',
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',cms.views.home,name='home'),
    url(r'^ajax/', include(djshop.ajax_urls)),
)


