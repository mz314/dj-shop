from rest_framework import serializers
from userdata.models import *

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    last_login=serializers.DateTimeField(required=False)
    date_joined=serializers.DateTimeField(required=False)
    class Meta:
        model=User
        fields=('id','is_superuser','username','password','first_name','last_name',
                'email','is_staff','is_active')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country



class UserDataSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    country=CountrySerializer()
    country_id=serializers.CharField()
    username=serializers.CharField()
    email=serializers.CharField()
    password=serializers.CharField()
    password2=serializers.CharField()
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)

    class Meta:
        model=UserData
        fields=('id','username','email','password','password2','first_name','last_name','country_id','city','zip','street','street_number')



    def save_object(self, obj, **kwargs):
        obj=UserData()

        user=User()
        user.username=self.init_data['username']
        user.first_name=self.init_data['first_name']
        user.last_name=self.init_data['last_name']
        user.email=self.init_data['email']
        user.set_password(self.init_data['password'])
        user.save()
        country=Country.objects.get(pk=self.init_data['country_id'])
        obj.user=user
        obj.country=country
        obj.street=self.init_data['street']
        obj.street_number=self.init_data['street_number']
        obj.city=self.init_data['city']
        obj.zip=self.init_data['zip']


        obj.save()









