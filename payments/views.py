from django.views.generic import TemplateView,View
from shop.models import *
from djshop.utils import *
from shop.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from shop.models import PaymentMethod
from payments.serializers import GatewaySerializer

class GatewayView(generics.ListAPIView):
    serializer_class = GatewaySerializer

    def get(self, request, *args, **kwargs):
        gw=PaymentMethod.objects.get(pk=kwargs['gw_id'])
        serializer=GatewaySerializer(gw)
        return Response(serializer.data)