from django.views.generic import TemplateView,View
from shop.models import *
from djshop.utils import *
from shop.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json




class CartView(generics.ListAPIView):
    serializer_class = CartSerializer


    def post(self,request,format=None,*args,**kwargs):
        try:
            item=Item.objects.get(pk=kwargs['item_id'])
        except Item.DoesNotExist:
            return Response('Wrong item_id',status=500)
        ci=CartItem(item=item,user=request.user,quantity=kwargs['quantity'])
        ci.save()
        return Response('OK')



    def get(self,request,*args,**kwargs):
        items = CartItem.objects.filter(user=request.user)
        serializer = CartSerializer(items, many=True)
        return Response(serializer.data)


class CartCheckoutAjax(CartView):


    def get(self,request,*args,**kwargs):
        status=OrderStatus()
        order=Order()
        order.user=request.user
        order.shipment=ShipmentMethod.objects.get(pk=kwargs['shipment_id'])
        order.payment=PaymentMethod.objects.get(pk=kwargs['payment_id'])
        order.save()
        status.status=OrderStatus.STATUS_PENDING
        status.order=order
        status.save()

        cart_items=CartItem.objects.filter(user=request.user)

        for ci in cart_items:
            i=OrderItem()
            i.fromItem(ci)
            i.order=order
            i.save()

        CartItem.objects.filter(user=request.user).delete()

        return HttpResponse(str(order.pk))

class CartCheckout(generics.ListAPIView):
    serializer_class = CartSerializer

    def post(self,request,*args,**kwargs):
        status=OrderStatus()
        order=Order()
        order.user=request.user
        order.shipment=ShipmentMethod.objects.get(pk=kwargs['shipment_id'])
        order.payment=PaymentMethod.objects.get(pk=kwargs['payment_id'])
        order.net_price=0
        order.total_price=0
        order.save()
        status.status=OrderStatus.STATUS_PENDING
        status.order=order
        status.save()

        cart_items=CartItem.objects.filter(user=request.user)

        for i in request.DATA:
           for ci in cart_items:
               if i['id']==ci.pk:
                   ci.quantity=i['quantity']
                   ci.save()




        for ci in cart_items:
            i=OrderItem()
            i.fromItem(ci)
            i.order=order
            i.save()

        CartItem.objects.filter(user=request.user).delete()

        order.calculate()
        order.save()

        serializer=OrderSerializer(order)

        return Response(serializer.data)


class CartList(CartView):
    @staticmethod
    def MakeJson(items,key='itemdata'):
        json_items=[]
        for i in items:
            itm=i.__dict__
            if key:
                idata=itm[key].__dict__
            else:
                idata=itm
            del idata['_state']
            idata['price']=float(idata['price'])
            if key:
                itm[key]=idata
            else:
                itm=idata
            try:
                del itm['_state']
                del itm['_item_cache']
            except KeyError:
                pass
            print itm
            json_items.append(itm)
        return json_items



    def get(self,request,*args,**kwargs):
        from itertools import chain
        items=CartItem.objects.all()
        #items=[i for i in items]
        jsonitems=[]
        for i in items:
            i.itemdata=Item.objects.get(pk=i.item.pk)
            jsonitems.append(i)

        jsonitems=CartList.MakeJson(jsonitems)
        return HttpResponse(json.JSONEncoder().encode(jsonitems))

class CartClean(CartView):
    def get(self,request,*args,**kwargs):
        CartItem.objects.filter(user=request.user).delete()
        return HttpResponse("OK")


class CartShipment(CartView):
    def get(self,request,*args,**kwargs):
        methods=ShipmentMethod.objects.filter(enabled=True)
        jsonmethods=[]

        return HttpResponse(json.JSONEncoder().encode(CartList.MakeJson(methods,None)))





