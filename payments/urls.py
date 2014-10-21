from django.conf.urls import patterns, include, url


from payments.gateways import creditcard
from payments.gateways import dummy
from payments import views


urlpatterns = patterns('',
    url(r'creditcard/(?P<order_id>.+)$',creditcard.CreditCard.as_view()),
    url(r'dummy/(?P<order_id>.+)$',dummy.Dummy.as_view()),
    url(r'gateway/(?P<gw_id>.+)$',views.GatewayView.as_view()),
)
