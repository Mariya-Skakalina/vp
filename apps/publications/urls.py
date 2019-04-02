from django.urls import path
from .views import *

urlpatterns = [
    path('', PublicationsViews.as_view(), name='PublicationsViews'),
    path('public/<slug:pk>/', PublicDetailViews.as_view(), name='PublicDetailViews'),
    path('section/', SectionViews.as_view(), name='SectionViews'),
    path('section/<slug:pk>', SectionDetailView.as_view(), name='SectionDetailView'),
    path('section/topic/<slug:pk>', TopicDetailView.as_view(), name='TopicDetailView'),
    path('search/', SearchPublic.as_view(), name='SearchPublic'),
]