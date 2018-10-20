from django.urls import path
from .views import *

urlpatterns = [
    path('', Publications.as_view(), name='Publications'),
    path('public/<slug:pk>/', PublicDetail.as_view(), name='PublicDetail'),
]