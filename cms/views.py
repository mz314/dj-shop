from django.shortcuts import render
from cms.models import *

def article(request,id):
    art=Article.objects.get(pk=id)
    context={
        'article':art,
    }
    return render(request,'cms/article.html',context)