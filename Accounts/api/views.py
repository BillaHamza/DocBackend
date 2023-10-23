from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterUserSerializer,CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from Accounts.models import *


class CustomUserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['Email'] = user.email
        #token['Faculte'] = user.faculte.id

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




