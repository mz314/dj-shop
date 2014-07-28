from django.db import models

class category(models.Model):
    name=models.CharField(max_length=64,null=False,blank=False)
    description=models.TextField(max_length=1024,null=True,blank=True)

class article(models.Model):
    parent_category=models.ForeignKey(category)
    title=models.CharField(max_length=64,null=False,blank=False)
    content=models.TextField(max_length=99999,null=False,blank=False)
