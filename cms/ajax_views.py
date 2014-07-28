from django.shortcuts import render
from django.core import serializers
from cms.utils import *
from cms.models import *



def front_articles(request):
    articles=Article.objects.filter(on_front=True)
    return jret(articles)