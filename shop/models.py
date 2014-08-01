from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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



class Category(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField(blank=True,null=True)
    parent=models.ForeignKey("self",blank=True,null=True)

    def __unicode__(self):
        return self.name





class Item(models.Model):
    name=models.CharField(max_length=128)
    descripion=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    categories=models.ManyToManyField(Category)
    #images=models.ManyToManyField(ItemImage,null=True,blank=True)
    tax=models.ForeignKey(Tax,null=True,blank=True)
    currency=models.ForeignKey(Currency)



    def __unicode__(self):
        return self.name



class ItemImage(models.Model):
    file=models.FileField(upload_to='products',null=True,blank=True)
    title=models.CharField(max_length=128,blank=True,null=True)
    main_image=models.BooleanField(blank=True,default=False)
    item=models.ForeignKey(Item)

    def __unicode__(self):
        return self.title


class Order(models.Model):
    datetime=models.DateTimeField(auto_now=True)




class CartItem(models.Model):
    user=models.ForeignKey(User)
    item=models.ForeignKey(Item)
    quantity=models.PositiveIntegerField()
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        existing=CartItem.objects.filter(Q(user=self.user,item=self.item) & ~Q(pk=self.pk))
        if len(existing)>0:
            existing[0].quantity+=int(self.quantity)
            existing[0].save()
        else:
            super(CartItem,self).save()




