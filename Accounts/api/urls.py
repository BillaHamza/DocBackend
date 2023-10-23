from django.urls import path
from .views import MyTokenObtainPairView,CustomUserCreate,CustomUserList
from rest_framework_simplejwt.views import (TokenRefreshView,)


urlpatterns = [
    path('register/',CustomUserCreate.as_view(),name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',CustomUserList.as_view(),name='ListUsers'),
]


