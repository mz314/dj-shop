from rest_framework import serializers
from shop.models import *


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ('id', 'file', 'title', 'item', 'main_image')


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'descripion', 'price',)

    @property
    def data(self):

        data = super(ItemsSerializer, self).data
        newdata = []
        for d in data:
            try:
                d['image'] = unicode(ItemImage.objects.get(item_id=d['id'], main_image=True).file)

            except (ItemImage.DoesNotExist, AttributeError) as e:
                d['image'] = ''
            newdata.append(d)

        return newdata


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent',)


class CartSerializer(serializers.ModelSerializer):
    item=ItemsSerializer()
    class Meta:
        model=CartItem
        fields=('id','item','quantity',)

    def set_request(self,request):
        self.request=request

    def save_object(self, obj, **kwargs):
        obj=CartItem()
        obj.item_id=self.init_data['item_id']
        obj.quantity=self.init_data['quantity']
        obj.user=self.request.user
        obj.save()
        return obj



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentMethod

