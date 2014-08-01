from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from djshop.utils import *
from django.contrib.auth.models import User
from userdata.models import *
from userdata.forms import *
import json


@csrf_exempt
def create_user(request):
     in_data=json.loads(request.body)
     user=User()
     user.username=in_data['username']
     user.first_name=in_data['first_name']
     user.last_name=in_data['last_name']
     user.set_password(in_data['password'])
     user.save()
     userdata=UserData()
     userdata.address=in_data['address']
     userdata.city=in_data['city']
     userdata.country=Country.objects.get(pk=in_data['country'])
     userdata.zip=in_data['zip']
     userdata.user=user
     userdata.save()
     return HttpResponse(in_data['country'])
