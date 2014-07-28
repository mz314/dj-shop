from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=64,null=False,blank=False)
    description=models.TextField(max_length=1024,null=True,blank=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    parent_category=models.ForeignKey(Category)
    title=models.CharField(max_length=64,null=False,blank=False)
    content=models.TextField(max_length=99999,null=False,blank=False)

    def __unicode__(self):
        return self.title
