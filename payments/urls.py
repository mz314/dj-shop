from django.conf.urls import patterns, include, url


from payments.gateways import invoice


urlpatterns = patterns('',
    url(r'invoice',invoice.gateway),
)
