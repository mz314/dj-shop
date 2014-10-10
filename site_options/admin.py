from django.contrib import admin

from site_options.models import *


class SettingAdmin(admin.ModelAdmin):
    list_display=('key','value',)


admin.site.register(Setting, SettingAdmin)
