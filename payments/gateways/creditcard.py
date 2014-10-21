from django.shortcuts import render
from django.http.response import HttpResponse
from payments.gateways import abstract


class CreditCard(abstract.PaymentGWAbstract):
    def process(self):
        self.fields={}
        for f in self.data:
            self.fields[f['name']]=f['value']

        errors=[]

        if self.fields['card']=='error':
            errors=['wat?']

        return {'status':'OK',"errors":errors}