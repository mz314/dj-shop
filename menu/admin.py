from django.contrib import admin
from menu.models import *

class MenuItemInline(admin.StackedInline):
    model=MenuItem
    class Meta:
        pass

class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)

class MenuItemAdmin(admin.ModelAdmin):
    pass




admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuItem,MenuItemAdmin)

