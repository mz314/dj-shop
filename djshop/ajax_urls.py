from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import cms.ajax_views



urlpatterns = patterns('',



    url(r'^fronts/$',cms.ajax_views.front_articles),

)
