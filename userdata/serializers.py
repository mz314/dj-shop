from rest_framework import serializers
from userdata.models import *

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields=('id','user',)