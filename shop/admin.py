from django.contrib import admin
from shop.models import *

class ItemImageInline(admin.TabularInline):
    model=ItemImage


class CategoryAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    inlines=[
        ItemImageInline,
    ]


class TaxAdmin(admin.ModelAdmin):
    pass


class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Currency,CurrencyAdmin)