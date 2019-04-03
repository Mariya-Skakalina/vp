from django.urls import path
from .views import *

urlpatterns = [
    path('', UsersView.as_view(), name = 'UsersView'),
    path('signup/', UserSignUp.as_view(), name = 'UserSignUp'),
    path('login/', UserLogin.as_view(), name = 'UserLogin'),
    path('detail/<slug:pk>/', UserDetailView.as_view(), name='UserDetailView'),
    path('setting/<slug:pk>/', UserSet.as_view()),
    path('search/', SearchUser.as_view(), name='SearchUser'),
    path('partner/', UsersPartner.as_view(), name='UsersPartner'),
    path('my-publications/', UserPublic.as_view(), name='UserPublic'),
    path('my-not-publications/', UserNotPublic.as_view(), name='UserNotPublic'),
    path('add-public/', UserAddPublic.as_view(), name='UserAddPublic')
]