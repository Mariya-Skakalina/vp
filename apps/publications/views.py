from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Public


class Publications(ListView):
    model = Public
    template_name = 'publications/home.html'

    def get_queryset(self):
        next = self.model.objects.filter(publication=True).order_by('-date_time')
        return next

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublicDetail(DetailView):
    model = Public
    template_name = 'publications/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context