from django.shortcuts import render,redirect
from django.http import HttpResponse

from djshop.utils import *
from userdata.models import *
from userdata.forms import *
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout,login,authenticate

def create_user_form(request):
    uform=UserForm()
    form=UserDataForm()
    return HttpResponse(uform.as_p()+" "+form.as_p())


def logout_user(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def login_user(request):
    try:
        data=json.loads(request.body)
    except ValueError:
        return HttpResponse('3')
    un=data.get('username')
    pw=data.get('password')
    user = authenticate(username=un, password=pw)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.user=user
            return HttpResponse('0')
        else:
            return HttpResponse('1')
    else:
        return HttpResponse('2')



def login_user_http(request):
    un=request.GET.get('username')
    pw=request.GET.get('password')
    user = authenticate(username=un, password=pw)
    if user is not None:
        if user.is_active:
            login(request, user)
            #request.user=user
    return redirect('/')


def create_user(request):

    form=UserDataForm(form_name="userform")

    context={'form':form,}
    return render(request,"userdata/create.html",context)
