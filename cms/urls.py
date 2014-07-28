from django.conf.urls import patterns, include, url
import cms.views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^article/(?P<id>[0-9]+)/$',cms.views.article)

)
