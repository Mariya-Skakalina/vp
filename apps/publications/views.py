from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.list import MultipleObjectMixin
from .models import Public, Topic, Section
from .documents import PublicDocument


class PublicationsViews(ListView):
    model = Public
    template_name = 'publications/home.html'
    paginate_by = 20
    queryset = Public.objects.filter(publication=True).order_by('-date_time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def search_query(answer, filt):
    if filt:
        print(filt)
        return PublicDocument.search().filter('term', publication=True).filter("term", topic_public__id = 3).query('multi_match', query=answer, fields=['title', 'context']).execute()
    else:
        return PublicDocument.search().filter('term', publication=True).query('multi_match', query=answer, fields=['title', 'context']).execute()

class SearchPublic(TemplateView):
    template_name = 'publications/search_public.html'

    def get_context_data(self, **kwargs):
        search = super().get_context_data(**kwargs)
        if self.request.GET.get('id'):
            search['public'] = search_query(self.request.GET.get('answer'), {'topic_public__id': int(self.request.GET.get('id'))})
        else:
            search['public'] = search_query(self.request.GET.get('answer'), {})
        print(search['public'])
        return search


class SectionViews(ListView):
    model = Section
    template_name = 'sections/topic.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublicDetailViews(DetailView):
    model = Public
    template_name = 'publications/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Это раздел
class SectionDetailView(DetailView, MultipleObjectMixin):
    model = Section
    template_name = 'sections/topic_public.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        object_list = self.object.public_set.filter(section=self.kwargs['pk']).order_by('-date_time')
        context = super(SectionDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context

# Категория
class TopicDetailView(DetailView, MultipleObjectMixin):
    model = Topic
    template_name = 'sections/section_public.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        object_list = self.object.public_set.filter(topic_public=self.kwargs['pk']).order_by('-date_time')
        context = super(TopicDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context