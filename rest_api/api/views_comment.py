from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.serializer_comment import *
from apps.comment.models import Comment
from apps.user.models import User, Rating
from apps.publications.models import Public
from rest_framework.parsers import JSONParser


class CommentUser(APIView):

    def post(self, req, **kwargs):
        data = CommentSerializer(data=req.data)
        if data.is_valid():
            user = req.session['auth']
            result = User.objects.get(id=user)
            public = Public.objects.get(id=data.data['public_comment'])
            Comment(text=data.data['text'], public_comment=public, author_comment = result).save()
            return Response({'res': 'Комментарий добавлен'})
        else:
            return Response({'res': 'Что то пошло не так'})


class AnswerUser(APIView):

    def post(self, req, **kwargs):
        data = AnswerSerializer(data=req.data)
        if data.is_valid():
            result = User.objects.get(id=req.session['auth'])
            comment = Comment.objects.get(id=data.data['answer'])
            Comment(answer=comment, text=data.data['text'],  author_comment=result).save()
            return Response({'res': 'Комментарий добавлен'})
        else:
            return Response({'res': 'Что то пошло не так'})


class RatingView(APIView):
    parser_classes = (JSONParser,)
    def post(self, req, **kwargs):
        data = RatingSerializer(data=req.data)
        if data.is_valid():
            user = User.objects.get(id=req.session['auth'])
            if data.data.get('public'):
                public = Public.objects.get(id=data.data['public'])
                Rating(public=public, like=data.data['like'], user=user).save()
            else:
                comment = Comment.objects.get(id=data.data['comment'])
                Rating(comment=comment, like=data.data['like'], user=user).save()
            return Response({'res': 'Лайк добавлен'})
        else:
            return Response({'res': 'Что то пошло не так'})
