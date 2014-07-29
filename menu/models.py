from django.db import models

class Menu(models.Model):
    name=models.CharField(max_length=48)
    tag=models.CharField(max_length=16)
    def __unicode__(self):
        return self.name+' '+self.tag


class MenuItem(models.Model):
    label=models.CharField(max_length=64)
    link=models.CharField(max_length=128,blank=True,default='')
    enabled=models.BooleanField(blank=True,default=True)
    menu=models.ForeignKey(Menu)
    parent=models.ForeignKey("self",blank=True,null=True)

    def __unicode__(self):
        return self.label

