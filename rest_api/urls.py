from django.urls import path
from .views import *

urlpatterns = [
    path('user_reg/', UserRegistration.as_view(), name='UserRegistration'),
    path('user_login/', UserLogin.as_view(), name='UserLogin')
]