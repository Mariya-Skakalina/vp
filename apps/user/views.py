from django.views.generic import TemplateView, DetailView, ListView
from .models import User
from .documents import UserDocument
from apps.publications.models import Public, Section, Topic
from django.http import HttpResponseRedirect


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

class SearchUser(TemplateView):
    template_name = 'user/search_user.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['users'] = UserDocument.search().filter().query('multi_match', query=self.request.GET.get('answer'), fields=['nickname']).execute()
        return result

class UsersPartner(ListView):
    model = User
    template_name = 'user/partner.html'
    paginate_by = 30
    queryset = User.objects.filter(activate=True, partner=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserPublic(ListView):
    model = Public
    template_name = 'user/user-public.html'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(publication=True, author_id=self.request.session['auth'])

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx

class UserNotPublic(ListView):
    model = Public
    template_name = 'user/user-not-public.html'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.filter(publication=False, author_id=self.request.session['auth'])

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class UserAddPublic(TemplateView):
    template_name = 'user/add-public.html'

    def post(self, request, **kwargs):
        if ('title' in request.POST) and ('ctx' in request.POST):
            sections = Section.objects.filter(name=request.POST['section'])
            user = User.objects.get(id=request.session['auth'])
            topic = Topic.objects.filter(title=request.POST['topic'])
            publics = Public(title=request.POST['title'], ctx=request.POST['ctx'], author=user)
            publics.save()
            publics.section.set(sections)
            publics.topic_public.set(topic)
            publics.save()
            return HttpResponseRedirect('/users/my-not-publications/')
        context = super().post(request, **kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.filter()
        context['topic'] = Topic.objects.filter()
        return context