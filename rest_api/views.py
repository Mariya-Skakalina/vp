import crypt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from hmac import compare_digest as compare_hash
from apps.user.models import User
from .serializer import *
from django.http import HttpResponseRedirect


class UserRegistration(APIView):

    def post(self, req, **kwargs):
        data = UserSerializer(data=req.data)
        if data.is_valid():
            # data.save()
            User(**data.data).save()
            return HttpResponseRedirect('/user/signup/')
        else:
            return Response({'res':'Не прошло валидацию'})


class UserLogin(APIView):

    def post(self, req, **kwargs):
        user_login = UserLoginSerializer(data=req.data)
        if user_login.is_valid():
            user = User.objects.filter(email=user_login.data['email'], activate=True)
            if len(user)>0:
                # используется для рассшифровки хэшированного пароля
                if compare_hash(user[0].password, crypt.crypt(str(user_login.data['password']),settings.SECRET_KEY_2)):
                    req.session['auth'] = user[0].id
                    return Response({'res':'true'})
                return Response({'res':'false'})
            else:
                return Response({'res': 'Нет такого пользователя'})
        else:
            return Response({'res': 'Не правильно введены данные'})