from django import forms
from django.contrib.auth.models import User
from djangular.forms.angular_model import NgModelFormMixin
from djangular.forms import NgFormValidationMixin
from userdata.models import *

"""

class UserForm(NgModelFormMixin,NgFormValidationMixin,forms.ModelForm):
    passowrd=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    def __init__(self):
        super(UserForm,self).__init__()
        self.fields['username'].help_text=None
"""

class UserDataFormBasic(forms.ModelForm):
    class Meta:
        model=UserData
        fields=['country','city','zip','address']


class LoginForm(NgModelFormMixin,NgFormValidationMixin,forms.Form):
    username=forms.CharField(label="User name")
    password=forms.CharField(label="Password")
    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='login_user')
        super(LoginForm, self).__init__(*args, **kwargs)


class UserDataForm(NgModelFormMixin, NgFormValidationMixin,UserDataFormBasic):
    username=forms.CharField(label="Username")
    first_name=forms.CharField(label="First name")
    last_name=forms.CharField(label="Last name")
    email=forms.CharField(label="Email")
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")
    password2=forms.CharField(widget=forms.PasswordInput(),label="Repeat password")



    def __init__(self, *args, **kwargs):
        kwargs.update(scope_prefix='userdata')
        super(UserDataForm, self).__init__(*args, **kwargs)