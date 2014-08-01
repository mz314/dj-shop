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
        ci=CartItem(item=item,user=request.user,quantity=1)

        ci.save()
        return HttpResponse('OK')



class CartList(CartView):
    def get(self,request,*args,**kwargs):
        from itertools import chain
        items=CartItem.objects.all()
        #items=[i for i in items]
        jsonitems=[]
        for i in items:
            i.itemdata=Item.objects.get(pk=i.item.pk)
            i=i.ToJSON()

            jsonitems.append(i)

        return HttpResponse(json.JSONEncoder().encode(jsonitems))

class CartClean(CartView):
    def get(self,request,*args,**kwargs):
        self.reset(request)
        return HttpResponse("OK")