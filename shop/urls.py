from django.conf.urls import patterns, include, url

from shop import rest_views as rviews
from shop import cart_view as cviews

urlpatterns = patterns('',

url(r'^categories/(?P<parent_id>.+)$',rviews.CategoryView.as_view()),
url(r'^categories/',rviews.CategoryView.as_view()),
url(r'^items/(?P<category_id>.+)$',rviews.ItemsView.as_view()),
url(r'^cart/(?P<item_id>.+)/(?P<quantity>.+)$',cviews.CartView.as_view()),
url(r'^cart$',cviews.CartView.as_view())
)