from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import cms.ajax_views
import shop.views
import shop.cart_view


urlpatterns = patterns('',

    url(r'^fronts/$',cms.ajax_views.front_articles),
    url(r'^article/([0-9])',cms.ajax_views.article),
    url(r'^category/$',shop.views.category),
    url(r'^category/(?P<id>\w+)/$',shop.views.category),
    url(r'^items/$',shop.views.items),
    url(r'^items/(?P<cat_id>\w+)/$',shop.views.items),
    url(r'^item/(?P<id>\w+)/$',shop.views.item),
    url(r'^add_to_cart/(?P<id>\w+)/$',shop.cart_view.CartView.as_view()),
    url(r'^cart/$',shop.cart_view.CartList.as_view()),
    url(r'^cart/clean/$',shop.cart_view.CartClean.as_view()),
)
