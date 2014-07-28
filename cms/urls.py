from django.conf.urls import patterns, include, url
import cms.views
import cms.ajax_views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^article/(?P<id>[0-9]+)/$',cms.views.article,name='article'),
    url(r'^categories/',cms.views.categories,name='categories'),
    url(r'^category/(?P<id>[0-9]+)/$',cms.views.category,name='category'),



)
