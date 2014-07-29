from django.core import serializers
from django.http import HttpResponse
import json

def jsonize(objects):
    try:
        data=serializers.serialize('json',objects)
    except TypeError:
        data=serializers.serialize('json',[objects])
    return data


def jret(objects):
    data=jsonize(objects)
    return HttpResponse(data,mimetype='application/json')
