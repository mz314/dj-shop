from django.shortcuts import render
from shop.models import *
from djshop.utils import *

def items(request,cat_id=None):
    if cat_id is None:
        items=[]
    else:
        items=Item.objects.filter(categories__in=cat_id)
        newitems=[]
        for i in items:
            i.image='test'
            newitems.append(i)
        items=newitems
    return jret(items)

def category(request,id=None):
    categories=Category.objects.filter(parent=id)


    return jret(categories)


def itemImages(request,id):
    images=ItemImage.objects.filter(item_id=id)
    return jret(list(images))

def item(request,id):
    item=Item.objects.get(pk=id)

    return jret([item])




def addToCart(request,id):
    #initCart(request)
    pass


