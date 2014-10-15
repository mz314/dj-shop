from django.views.generic import TemplateView,View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from userdata.models import *
from userdata.serializers import *
from rest_framework import generics
from django.http import HttpResponse


class LoginCheckView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponse('1')
        else:
            return HttpResponse('0')




class UserDataView(generics.ListAPIView):
    serializer_class = UserDataSerializer

    def get_queryset(self):


        return UserData.objects.filter(user=self.request.user)


    def get(self, request, *args, **kwargs):


        if not request.user.is_authenticated():
            return Response("0")

        serializer = UserSerializer(request.user, many=False)
        return Response(serializer.data)
