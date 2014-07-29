from django.views.generic import TemplateView,View
from shop.models import *
from djshop.utils import *
import json


class CartView(View):
    def initCart(self,request):
        try:
            tmp=request.session['cart']
        except KeyError:
            self.reset(request)

    def reset(self,request):
        request.session['cart']=""

    def get_cotents(self,request):
        contents=request.session['cart']
        if contents=="":
            return list()
        try:
            contents=json.JSONDecoder().decode(contents)
        except TypeError:
            self.reset(request)
            contents=[]
        return contents

    def update(self,request,cart):
        cart=json.JSONEncoder().encode(cart)
        request.session['cart']=cart

    def add(self,request,item):
        cart=self.get_cotents(request)
        cart.append(item)
        self.update(request,cart)

    def get(self,request,*args,**kwargs):
        self.initCart(request)
        self.add(request,kwargs['id'])
        print request.session['cart']
        return HttpResponse('OK')



class CartList(CartView):
    def get(self,request,*args,**kwargs):
        cart=self.get_cotents(request)
        items=Item.objects.filter(pk__in=cart)
        return jret(items)


class CartClean(CartView):
    def get(self,request,*args,**kwargs):
        self.reset(request)
        return HttpResponse("OK")