from django.db import models


class Tax(models.Model):
    name=models.CharField(max_length=64)
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    def __unicode__(self):
        return self.name+' '+unicode(self.amount)+'%'

class Currency(models.Model):
    name=models.CharField(max_length=128)
    symbol=models.CharField(max_length=16)
    factor=models.DecimalField(decimal_places=2,max_digits=10)


class Category(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField(blank=True,null=True)
    parent=models.ForeignKey("self",blank=True,null=True)

    def __unicode__(self):
        return self.name



class ItemImage(models.Model):
    #file=models.FileField()
    title=models.CharField(max_length=128,blank=True,null=True)
    main=models.BooleanField(blank=True,default=False)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    name=models.CharField(max_length=128)
    descripion=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    categories=models.ManyToManyField(Category)
    images=models.ManyToManyField(ItemImage,null=True,blank=True)
    tax=models.ForeignKey(Tax,null=True,blank=True)
    currency=models.ForeignKey(Currency)


    def __unicode__(self):
        return self.name










