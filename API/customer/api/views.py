from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST 
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    DataCatcherSerializer,
    DataUpdateSerializer
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from customer.models import Customer
from rest_framework import viewsets
# Create your views here.
User=get_user_model()

class UserCreateAPIView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=UserCreateSerializer
    queryset=User.objects.all()
    

class UserLoginAPIView(APIView):
    permission_classes=[AllowAny]
    serializer_class=UserLoginSerializer

    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DataManView(APIView):
    #permission_classes=[AllowAny]
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class=DataCatcherSerializer
    
    def get(self,request,*args,**kwargs):
        Customer1=Customer.objects.all()
        serializer=DataCatcherSerializer(Customer1,many=True)
        return Response(serializer.data)
    

    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=DataCatcherSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            serializer.create(new_data)
            return Response(new_data, status=HTTP_200_OK)    
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class DataUpdateView(APIView):
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class=DataUpdateSerializer

    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=DataUpdateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            serializer.create(new_data)
            return Response(new_data, status=HTTP_200_OK)    
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)