from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework import routers

from shop import rest_views as sviews

admin.autodiscover()
import cms.views
import userdata.rest_urls
import userdata.urls
import djshop.ajax_urls
import shop.urls



#router = routers.DefaultRouter()
#router.register(r'categories',sviews.CategoryViewSet)



urlpatterns = patterns('',
    url(r'^api/', include(shop.urls)),
    url(r'^api/user', include(userdata.rest_urls)),
    url(r'^user/', include(userdata.urls)),
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',cms.views.home,name='home'),
    url(r'^ajax/', include(djshop.ajax_urls)),
    url(r'^api/payment',include('payments.urls'))
    #url(r'^user/',include(userdata.urls))
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))



