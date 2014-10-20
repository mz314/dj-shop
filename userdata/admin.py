from django.contrib import admin
from userdata.models import *

class CountryAdmin(admin.ModelAdmin):
    pass

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','email']

    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name

    def email(self,obj):
        return obj.user.email

admin.site.register(Country,CountryAdmin)
admin.site.register(UserData,UserDataAdmin)
