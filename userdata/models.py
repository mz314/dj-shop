from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name=models.CharField(max_length=128)
    code=models.CharField(max_length=16)

    def __unicode__(self):
        return self.name


class UserData(models.Model):
    user=models.ForeignKey(User)
    country=models.ForeignKey(Country)
    city=models.CharField(max_length=128)
    zip=models.CharField(max_length=16)
    street=models.CharField(max_length=128)
    street_number=models.CharField(max_length=128)

    def __unicode__(self):
        return self.user.username+" "+self.user.first_name+" "+self.user.last_name+" "+self.user.email


