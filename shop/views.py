from django.shortcuts import render
from shop.models import *
from djshop.utils import *

def items(request,cat_id=None):
    items=Item.objects.filter(categories__in=cat_id)
    return jret(items)

def category(request,id=None):
    categories=Category.objects.filter(parent=id)


    return jret(categories)