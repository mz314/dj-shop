from django.conf import settings
import json


def loadJson(name):
    f=open(settings.BASE_DIR+'/payments/gateways/'+name)
    contents = json.load(f)
    f.close()
    return contents