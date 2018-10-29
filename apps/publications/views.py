from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Public, Topic, Section


class PublicationsViews(ListView):
    model = Public
    template_name = 'publications/home.html'
    publication_list = Public.objects.filter(publication=True).order_by('-date_time')


    # def get_queryset(self):
    #     paginator = Paginator(publication_list, 2, orphans=1)
    #     page = self.request.GET.get('page')
    #     try:
    #         if page != None:
    #             publication_list = paginator.get_page(page)
    #         else:
    #             publication_list = paginator.get_page(2)
    #     except EmptyPage:
    #         publication_list = paginator.get_page(paginator.num_pages)
    #     except PageNotAnInteger:
    #         publication_list = paginator.get_page(2)
    #     return publication_list
    #     return next

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublicDetailViews(DetailView):
    model = Public
    template_name = 'publications/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TopicViews(ListView):
    model = Topic
    template_name = 'sections/topic.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'sections/topic_public.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public'] = Public.objects.filter(section__topic = self.kwargs['pk']).order_by('-date_time')
        return context


class SectionDetailView(DetailView):
    model = Section
    template_name = 'sections/section_public.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public'] = Public.objects.filter(section=self.kwargs['pk']).order_by('-date_time')
        return context