from django.views.generic import TemplateView,View
from django.shortcuts import render
from django.http.response import HttpResponse
from shop.models import Order,OrderStatus
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics
import json

class PaymentGWAbstract(generics.GenericAPIView):

    def process(self):
        return 'Empty'

    def success(self):
        status=OrderStatus()
        status.status=OrderStatus.STATUS_PAYED
        status.order=self.order
        status.save()

    def post(self,request,*args,**kwargs):
        self.data=request.DATA

        self.order=Order.objects.get(pk=kwargs['order_id'])
        self.request=request
        self.args=args
        self.kwargs=kwargs
        resp=self.process()
        if not resp['errors']:
            self.success()


        return HttpResponse(json.dumps(resp))
