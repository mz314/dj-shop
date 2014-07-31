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
    # return HttpResponse(in_data)

     user=User()
     user.username=in_data['username']
     user.first_name=in_data['first_name']
     user.last_name=in_data['last_name']
     user.set_password(in_data['password'])
     user.save()
     return HttpResponse('OK')