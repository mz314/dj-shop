from django.conf.urls import patterns, include, url

from shop import rest_views as rviews
from shop import cart_view as cviews
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',

url(r'^categories/(?P<parent_id>.+)$',rviews.CategoryView.as_view()),
url(r'^categories/',rviews.CategoryView.as_view()),
url(r'^ctree/',rviews.CategoryRecursiveView.as_view()),
url(r'^items/(?P<category_id>.+)$',rviews.ItemsView.as_view()),
url(r'^item/(?P<item_id>.+)$',rviews.ItemView.as_view()),
url(r'^cart/(?P<item_id>.+)/(?P<quantity>.+)$',cviews.CartView.as_view()),
url(r'^cart$',cviews.CartView.as_view()),
url(r'orders/(?P<order_id>.+)$',rviews.OrdersView.as_view()),
url(r'orders',rviews.OrdersView.as_view()),
url(r'^payment_list$',rviews.PaymentMethodView.as_view()),
url(r'^checkout/(?P<shipment_id>\w+)/(?P<payment_id>\w+)$',cviews.CartCheckout.as_view()),
)