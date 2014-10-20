from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from shop.models import *
from shop.serializers import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

class CategoryView(generics.ListAPIView):
    #queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            parent_id = self.kwargs['parent_id']
            return Category.objects.filter(parent_id=parent_id)
        except KeyError:
            return Category.objects.filter(parent_id=None)





class ItemsView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        try:
            category_id=self.kwargs['category_id']
            return Item.objects.filter(categories__in=[category_id,])
        except KeyError:
            return Item.objects.all()



class PaymentMethodView(generics.ListAPIView):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()


class OrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @csrf_exempt
    def post(self,request, *args, **kwargs):
        pass

