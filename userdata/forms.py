from django import forms
from django.contrib.auth.models import User
from userdata.models import *




class UserForm(forms.ModelForm):
    passowrd=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    def __init__(self):
        super(UserForm,self).__init__()
        self.fields['username'].help_text=None



class UserDataForm(forms.ModelForm):
    class Meta:
        model=UserData
        fields=['country','city','zip','address']


