from django.db import models

class Setting(models.Model):
    SETTING_CHOICES=(
        ('shop_name','Shop name'),
    )
    key=models.CharField(max_length=128,choices=SETTING_CHOICES,verbose_name=u"Option")
    value=models.CharField(max_length=128,verbose_name=u"Value")

    def __unicode__(self):
        return self.value