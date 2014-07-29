from djshop.utils import *
from cms.models import *



def front_articles(request):
    articles=Article.objects.filter(on_front=True)
    return jret(articles)

def article(request,id):
    art=Article.objects.get(pk=id)
    return jret(art)