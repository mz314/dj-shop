from rest_framework import serializers

from cms.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
