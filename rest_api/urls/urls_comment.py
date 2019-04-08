from django.urls import path
from rest_api.api.views_comment import *
# from rest_framework import routers
# routers.SimpleRouter()

urlpatterns = [
    path('comment/', CommentUser.as_view(), name='CommentUser'),
    path('answer/', AnswerUser.as_view(), name='AnswerUser'),
    path('rating/', RatingView.as_view(), name='RatingView')
]