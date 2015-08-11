from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics

from cms.serializers import *
from cms.models import *

class ArticleView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer



