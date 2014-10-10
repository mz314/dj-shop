from django.views.generic import TemplateView,View
from shop.models import *
from djshop.utils import *
import json



"""class CartItem(object):
    def __init__(self,pk,quantity=1):
        self.pk=pk
        self.SetQuantity(quantity)

    def inc(self,n=1):
        self.quantity+=n

    def SetQuantity(self,n):
        self.quantity=n
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
"""

class CartView(View):


    def get(self,request,*args,**kwargs):

        item=Item.objects.get(pk=kwargs['id'])
        ci=CartItem(item=item,user=request.user,quantity=kwargs['quantity'])

        ci.save()
        return HttpResponse('OK')



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


class CartCheckout(CartView):
    def get(self,request,*args,**kwargs):

        order=Order()
        order.user=request.user
        order.shipment=ShipmentMethod.objects.get(pk=kwargs['shipment_id'])
        order.save()

        cart_items=CartItem.objects.filter(user=request.user)

        for ci in cart_items:
            i=OrderItem()
            i.fromItem(ci)
            i.order=order
            i.save()

        CartItem.objects.filter(user=request.user).delete()

        return HttpResponse("OK")