from django.urls import path
from .views import *

urlpatterns = [
    path('user_reg/', UserRegistration.as_view(), name='UserRegistration'),
    path('user_login/', UserLogin.as_view(), name='UserLogin'),
    path('user_settings/', UserSettings.as_view(), name='UserSettings')
]