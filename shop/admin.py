from django.contrib import admin
from shop.models import *

class ItemImageInline(admin.TabularInline):
    model=ItemImage
    extra=0

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


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('name','enabled')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',)

class OrderItemInline(admin.StackedInline):
    model=OrderItem

class OrderStatusInline(admin.StackedInline):
    model=OrderStatus

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline,OrderStatusInline,]
    list_display = ('pk','user','datetime')

admin.site.register(Order,OrderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(ShipmentMethod,ShipmentAdmin)
admin.site.register(PaymentMethod,PaymentAdmin)