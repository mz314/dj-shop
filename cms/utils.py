from django.core import serializers
from django.http import HttpResponse

def jsonize(objects):
    data=serializers.serialize('json',objects)
    return data


def jret(objects):
    data=jsonize(objects)
    return HttpResponse(data,mimetype='application/json')
