from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
