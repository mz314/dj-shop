from django.contrib import admin
from shop.models import *

class CategoryAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class TaxAdmin(admin.ModelAdmin):
    pass



admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Tax,TaxAdmin)