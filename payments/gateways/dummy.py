from django.shortcuts import render
from django.http.response import HttpResponse
from payments.gateways import abstract


class Dummy(abstract.PaymentGWAbstract):
    def process(self):
        return {'status':'OK','errors':[]}