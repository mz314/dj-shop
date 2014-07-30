from django.shortcuts import render
from django.http import HttpResponse

from djshop.utils import *
from userdata.models import *
from userdata.forms import *

def create_user_form(request):
    uform=UserForm()
    form=UserDataForm()
    return HttpResponse(uform.as_p()+" "+form.as_p())
