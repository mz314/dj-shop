from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from userdata.models import *
from userdata.serializers import *
from rest_framework import generics



class UserDataView(generics.ListAPIView):
    serializer_class = UserDataSerializer

    def get_queryset(self):


        return UserData.objects.filter(user=self.request.user)
