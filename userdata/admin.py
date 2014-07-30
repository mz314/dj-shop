from django.contrib import admin
from userdata.models import *

class CountryAdmin(admin.ModelAdmin):
    pass

class UserDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country,CountryAdmin)
admin.site.register(UserData,UserDataAdmin)
