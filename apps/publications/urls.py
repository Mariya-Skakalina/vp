from django.urls import path
from .views import *

urlpatterns = [
    path('', PublicationsViews.as_view(), name='PublicationsViews'),
    path('public/<slug:pk>/', PublicDetailViews.as_view(), name='PublicDetailViews'),
    path('topic/', TopicViews.as_view(), name='TopicViews'),
    # path('users/', Users.as_view(), name='Users'),
    # path('sections/<slug:pk>', TopicView.as_view(), name='topic_progr'),
    # path('sections/topic/<slug:pk>', TopicPublic.as_view(), name='TopicPublic')
    # path('search/', Search.as_view(), name='Search'),
]