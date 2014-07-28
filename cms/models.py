from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=64,null=False,blank=False)
    description=models.TextField(max_length=1024,null=True,blank=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    parent_category=models.ForeignKey(Category,null=True,blank=True)
    title=models.CharField(max_length=64,null=False,blank=False)
    content=models.TextField(max_length=99999,null=False,blank=False)
    on_front=models.BooleanField(blank=True,default=False)

    def __unicode__(self):
        return self.title

    def short(self):
        max_l=100
        if(len(self.content)>max_l):
            s=self.content[:max_l]+'...'
            return s
        else:
            return self.content
