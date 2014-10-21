from rest_framework import serializers
from shop.models import PaymentMethod
from payments.utils import *



class GatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod


    def to_native(self, obj):
        native=super(GatewaySerializer,self).to_native(obj)
        native['config']=loadJson(native['config'])
        print native
        return native

