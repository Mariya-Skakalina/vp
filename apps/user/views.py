from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
from django.views import View
from .models import User


class UserSignUp(TemplateView):
    template_name = 'user/signup.html'


class UserLogin(TemplateView):
    template_name = 'user/login.html'


class UserSet(DetailView):
    model = User
    template_name = 'user/user_set.html'

class UsersView(ListView):
    model = User
    template_name = 'user/users.html'
    paginate_by = 30
    queryset = User.objects.filter(activate=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

