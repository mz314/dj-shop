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



