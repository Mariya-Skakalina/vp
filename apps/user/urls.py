from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersView.as_view(), name = 'UsersView'),
    path('signup/', UserSignUp.as_view(), name = 'UserSignUp'),
    path('login/', UserLogin.as_view(), name = 'UserLogin'),
    path('detail/<slug:pk>/', UserDetailView.as_view(), name='UserDetailView'),
    path('setting/<slug:pk>/', UserSet.as_view())

]