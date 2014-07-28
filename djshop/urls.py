from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
import cms.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cms/', include('cms.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',cms.views.test,name='test')
    )

# urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
