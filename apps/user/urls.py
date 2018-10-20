from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', UserSignUp.as_view(), name ='UserSignUp'),
    path('login/', UserLogin.as_view(), name='UserLogin')
]