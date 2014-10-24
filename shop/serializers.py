from rest_framework import serializers
from shop.models import *


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ('id', 'file', 'title', 'item', 'main_image')

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tax

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model=Currency


class ItemsSerializer(serializers.ModelSerializer):
    tax_price=serializers.DecimalField(max_digits=10,decimal_places=8)
    tax=TaxSerializer()
    currency=CurrencySerializer()
    class Meta:
        model = Item
        fields = ('id', 'name', 'descripion', 'price','tax_price','tax','currency',
                  'weight','width','height','depth')

    @property
    def data(self):

        data = super(ItemsSerializer, self).data
        newdata = []
        if not isinstance(data,list):
            data=[data]
        for d in data:
            d['images'] = ItemImageSerializer(ItemImage.objects.filter(item_id=d['id']),many=True).data
            try:
                d['image'] = ItemImageSerializer(ItemImage.objects.get(item_id=d['id'], main_image=True),many=False).data

            except (ItemImage.DoesNotExist, AttributeError) as e:
                d['image'] = ''
            newdata.append(d)

        return newdata


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent',)

class CategorySerializerRecursive(CategorySerializer):

    def to_native(self, obj):
        native=super(CategorySerializerRecursive,self).to_native(obj)
        children=Category.objects.filter(parent_id=obj.pk)
        #cs=CategorySerializerRecursive(children)
        print len(children)
        sc=[]
        if len(children)>0:
            for c in children:
                n=self.to_native(c)
                sc.append(n)
        #print self.to_native(CategorySerializerRecursive(children))
        native['children']=sc #list(children)
        return native





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


class OrderItemSerializer(serializers.ModelSerializer):
    item=ItemsSerializer()
    class Meta:
        model=OrderItem
        fields = ('id','item','quantity')


class ShipmentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShipmentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentMethod


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set=OrderItemSerializer(many=True)
    payment=PaymentMethodSerializer()
    shipment=ShipmentMethodSerializer()
    #status=serializers.CharField(read_only=True)
    class Meta:
        model=Order
        fields=('id','datetime','user','shipment','payment','net_price','total_price','orderitem_set',)

    def to_native(self, obj):
        native=super(OrderSerializer,self).to_native(obj)
        stat=OrderStatus.get_newest(obj)
        native['status']=stat.status
        native['text_status']=stat.textual()
        return native





