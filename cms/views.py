from django.shortcuts import render
from cms.models import *

def article(request,id):
    art=Article.objects.get(pk=id)
    context={
        'article':art,
    }
    return render(request,'cms/article.html',context)


def categories(request):
    cats=Category.objects.all()
    context={
        'categories':cats,
    }
    return render(request,'cms/categories.html',context)


def category(request,id):
    arts=Article.objects.filter(parent_category=id)
    context={
        'articles':arts,
    }
    return render(request,'cms/category.html',context)