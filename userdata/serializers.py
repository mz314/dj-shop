from rest_framework import serializers
from userdata.models import *

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','last_login','is_superuser','first_name','last_name','email','is_staff','is_active','date_joined','groups','user_permissions')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country

class UserDataSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    country=CountrySerializer()
    class Meta:
        model=UserData
        #fields=('id','user',)