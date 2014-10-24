from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Max
import json



class Tax(models.Model):
    name=models.CharField(max_length=64)
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    def __unicode__(self):
        return self.name+' '+unicode(self.amount)+'%'

class Currency(models.Model):
    name=models.CharField(max_length=128)
    symbol=models.CharField(max_length=16)
    factor=models.DecimalField(decimal_places=2,max_digits=10)

    def __unicode__(self):
        return self.name+" (%s)" % (self.symbol,)


class Priced(models.Model):
    class Meta:
        abstract=True
    price=models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True,default=0.0)
    tax=models.ForeignKey(Tax,null=True,blank=True)
    currency=models.ForeignKey(Currency,null=True,blank=True)

    @property
    def tax_price(self):
        if self.tax:
            price=self.price*(self.tax.amount/100)+self.price
            return price
        else:
            return self.price

class Category(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField(blank=True,null=True)
    parent=models.ForeignKey("self",blank=True,null=True)

    def __unicode__(self):
        return self.name






class Item(Priced):
    name=models.CharField(max_length=128)
    descripion=models.TextField(blank=True,null=True)
    weight=models.DecimalField(verbose_name=u"Weight (kg)",max_digits=10,decimal_places=8,null=True,blank=True,default=None)
    width=models.DecimalField(verbose_name=u"Width (m)",max_digits=10,decimal_places=8,null=True,blank=True,default=None)
    height=models.DecimalField(verbose_name=u"Height (m)",max_digits=10,decimal_places=8,null=True,blank=True,default=None)
    depth=models.DecimalField(verbose_name=u"Depth (m)",max_digits=10,decimal_places=8,null=True,blank=True,default=None)
    categories=models.ManyToManyField(Category)
    #images=models.ManyToManyField(ItemImage,null=True,blank=True)


    def __unicode__(self):
        return self.name



class ItemImage(models.Model):
    file=models.FileField(upload_to='products',null=True,blank=True)
    title=models.CharField(max_length=128,blank=True,null=True)
    main_image=models.BooleanField(blank=True,default=False)
    item=models.ForeignKey(Item)

    def __unicode__(self):
        return self.title


class ShipmentMethod(Priced):
    name=models.CharField(max_length=128,blank=False,null=False)
    enabled=models.BooleanField(blank=True,default=True)
    def __unicode__(self):
        return self.name


class PaymentMethod(Priced):
    name=models.CharField(max_length=128,verbose_name=u"Payment name")
    config=models.CharField(max_length=256,verbose_name=u"Config file")


class ItemAbs(models.Model):
    class Meta:
        abstract=True

    item=models.ForeignKey(Item)
    quantity=models.PositiveIntegerField()

    def fromItem(self,other_item):
        self.item=other_item.item
        self.quantity=other_item.quantity



class CartItem(ItemAbs):
    user=models.ForeignKey(User)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        existing=CartItem.objects.filter(Q(user=self.user,item=self.item) & ~Q(pk=self.pk))
        if len(existing)>0:
            existing[0].quantity+=int(self.quantity)
            existing[0].save()
        else:
            super(CartItem,self).save()



class Order(models.Model):
    datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=False)
    shipment=models.ForeignKey(ShipmentMethod)
    payment=models.ForeignKey(PaymentMethod)
    net_price=models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Total net price")
    total_price=models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Total price")

    def calculate(self):
        net_sum=0
        sum=0
        items=OrderItem.objects.filter(order=self)
        for i in items:
            sum+=i.item.tax_price
            net_sum+=i.item.price
        self.net_price=net_sum
        self.total_price=sum

    def __unicode__(self):
        return self.pk



class OrderStatus(models.Model):
    STATUS_PENDING=0
    STATUS_PAYED=1
    STATUS_SENT=2
    STATUS_CHOICES=(
        (STATUS_PENDING,u'Awaiting payment'),
        (STATUS_PAYED,u'Payed'),
        (STATUS_SENT,u'Sent')
    )
    datetime=models.DateTimeField(auto_now=True)
    order=models.ForeignKey(Order)
    status=models.CharField(max_length=64,choices=STATUS_CHOICES)

    def textual(self):
        for s in OrderStatus.STATUS_CHOICES:
            (n,t)=s

            if str(n)==self.status or n==self.status:
                return t

        return unicode(self.status)

    @staticmethod
    def get_newest(order):
        objects=OrderStatus.objects.filter(order=order).order_by('-datetime')
        #print objects
        try:
            #print 'a'
            return objects[0]
        except IndexError:
            #print 'b'
            return OrderStatus(status=OrderStatus.STATUS_PENDING)




class OrderManager(models.Manager):
    def get_queryset(self):
        return super(Order,self).get_queryset()


class OrderItem(ItemAbs):
    order=models.ForeignKey(Order)














