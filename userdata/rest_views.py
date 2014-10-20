from django.views.generic import TemplateView,View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from userdata.models import *
from userdata.serializers import *
from rest_framework import generics
from django.http import HttpResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins

class LoginCheckView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponse('1')
        else:
            return HttpResponse('0')



class CountriesView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class UserDataView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    serializer_class = UserDataSerializer

    def get_queryset(self):


        return UserData.objects.filter(user=self.request.user)

    @csrf_exempt
    def post(self,request, *args, **kwargs):
        #return self.create(request, *args, **kwargs)
        udserializer=UserDataSerializer(None,request.DATA)
        if udserializer.is_valid():
            udserializer.save()
            return Response(udserializer.data)
        else:
            return Response(udserializer.errors,status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):


        if not request.user.is_authenticated():
            return Response("0")

        serializer = UserSerializer(request.user, many=False)
        return Response(serializer.data)
