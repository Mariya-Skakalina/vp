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
            print(data.data)
            # data.save()
            User(**data.data).save()
        else:
            return HttpResponseRedirect('/user/signup/')


class UserLogin(APIView):

    def post(self, req, **kwargs):
        user_login = UserLoginSerializer(data=req.POST)
        if user_login.is_valid():
            user = User.objects.filter(email=user_login.data['email'], activate=True)
            if len(user)>0:
                # используется для рассшифровки хэшированного пароля
                if compare_hash(user[0].password, crypt.crypt(str(user_login.data['password']),settings.SECRET_KEY_2)):
                    req.session['auth'] = user_login[0].id
                    return Response({'res':'true'})
                return Response({'res':'false'})
        else:
            return HttpResponseRedirect('/user/login/')