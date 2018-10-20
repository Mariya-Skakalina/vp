from django.shortcuts import render
from django.views.generic import TemplateView


class UserSignUp(TemplateView):
    template_name = 'user/signup.html'

    def post(self, req, *args, **kwargs):
        ctx = super(UserSignUp, self).get(req, *args, **kwargs)
        return ctx


class UserLogin(TemplateView):
    template_name = 'user/login.html'

    def post(self, req, *args, **kwargs):
        ctx = super(UserLogin, self).get(req, *args, **kwargs)
        return ctx