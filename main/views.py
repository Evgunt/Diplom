import os

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView, DetailView, ListView
from . import models, forms
from post_office import mail
from easyauth.settings import MEDIA_ROOT, DEFAULT_FROM_EMAIL


class UserLogin(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next_page = '/mydocs'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'
    login_url = '/'
    next_page = '/'


class Registration(CreateView):
    model = models.AdvUser
    template_name = 'auth/registration.html'
    form_class = forms.RegisterUserForm
    success_url = '/mydocs'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = models.AdvUser.objects.get(pk=self.request.user.pk)
        user.dateBorn = self.dateFormat(user.dateBorn)
        context['info'] = user
        return context

    def dateFormat(self, date):
        newdate = date.split('-')
        new = newdate[2] + '.' + newdate[1] + '.' + newdate[0]
        return new


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = models.AdvUser
    template_name = 'profile/userDetail.html'

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        user = get_object_or_404(queryset, pk=pk)
        user.dateBorn = self.dateFormat(user.dateBorn)
        return user

    def dateFormat(self, date):
        newdate = date.split('-')
        new = newdate[2] + '.' + newdate[1] + '.' + newdate[0]
        return new


class ChangeUser(UpdateView, LoginRequiredMixin):
    model = models.AdvUser
    template_name = 'profile/changeProfile.html'
    form_class = forms.ChangeUserForm
    success_url = '/mydocs'
    login_url = '/'
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        user = get_object_or_404(queryset, pk=pk)
        return user


class ChangePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/changePass.html'
    success_url = '/mydocs'
    login_url = '/'


class MyDocs(LoginRequiredMixin, ListView):
    template_name = 'profile/mydocs.html'
    login_url = '/'
    model = models.DocsFile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if models.DocsFile.objects.filter(owner=self.request.user.username).exists():
            userDocs = ''
            if 'filter' in self.request.GET:
                if self.request.GET['filter'] == 'name':
                    userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('name')
                elif self.request.GET['filter'] == 'old':
                    userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('pk')
            else:
                userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('-pk')

            paginator = Paginator(userDocs, 4)
            if 'page' in self.request.GET:
                page_num = self.request.GET['page']
            else:
                page_num = 1
            userDocs = paginator.get_page(page_num)

            context['info'] = userDocs
        return context


class PublicDocs(LoginRequiredMixin, ListView):
    template_name = 'profile/publicdocs.html'
    login_url = '/'
    model = models.DocsFile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if models.DocsFile.objects.filter(status=True).exists():
            userDocs = ''
            if 'filter' in self.request.GET:
                if self.request.GET['filter'] == 'name':
                    userDocs = models.DocsFile.objects.filter(status=True).order_by('name')
                elif self.request.GET['filter'] == 'old':
                    userDocs = models.DocsFile.objects.filter(status=True).order_by('pk')
            else:
                userDocs = models.DocsFile.objects.filter(status=True).order_by('-pk')

            paginator = Paginator(userDocs, 4)
            if 'page' in self.request.GET:
                page_num = self.request.GET['page']
            else:
                page_num = 1
            userDocs = paginator.get_page(page_num)

            context['info'] = userDocs
        return context


class DocsAdd(LoginRequiredMixin, CreateView):
    model = models.DocsFile
    template_name = 'profile/docsAdd.html'
    form_class = forms.DocsAddForm
    success_url = '/mydocs'

    def post(self, request, *args, **kwargs):
        form = forms.DocsAddForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.docs = request.FILES['docs']
            instance.extension = request.FILES['docs'].name.split('.')[-1]
            instance.save()
        return HttpResponseRedirect('/mydocs')


class DocsDelete(LoginRequiredMixin, DeleteView):
    model = models.DocsFile
    template_name = 'profile/deleteDocs.html'
    success_url = '/mydocs'


class DocsEdit(LoginRequiredMixin, UpdateView):
    model = models.DocsFile
    template_name = 'profile/changeDocs.html'
    form_class = forms.ChangeDocsForm
    success_url = '/mydocs'
    login_url = '/'
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        docs = get_object_or_404(queryset, pk=pk)
        return docs


class Search(LoginRequiredMixin, TemplateView):
    template_name = 'profile/search.html'
    login_url = '/'

    def post(self, request, *args, **kwargs):
        key = request.POST['key']
        context = {}
        if models.DocsFile.objects.filter(Q(name__iregex=key, owner=request.user)
                                          | Q(name__iregex=key, status=True)).exists():
            userDocs = models.DocsFile.objects.filter(Q(name__iregex=key, owner=request.user)
                                                      | Q(name__iregex=key, status=True)).order_by('-pk')

            paginator = Paginator(userDocs, 4)
            if 'page' in self.request.GET:
                page_num = self.request.GET['page']
            else:
                page_num = 1
            context['info'] = paginator.get_page(page_num)
            context['key'] = key

        else:
            context['message'] = 'По вашему запросу ничего не найдено'
        return render(request, 'profile/search.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'key' in self.request.GET:
            key = self.request.GET['key']
            if models.DocsFile.objects.filter(Q(name__iregex=key, owner=self.request.user)
                                              | Q(name__iregex=key, status=True)).exists():
                userDocs = models.DocsFile.objects.filter(Q(name__iregex=key, owner=self.request.user)
                                                          | Q(name__iregex=key, status=True)).order_by('-pk')

                paginator = Paginator(userDocs, 4)
                if 'page' in self.request.GET:
                    page_num = self.request.GET['page']
                else:
                    page_num = 1
                context['info'] = paginator.get_page(page_num)
                context['key'] = key
            else:
                context['message'] = 'По вашему запросу ничего не найдено'
        return context


class EmailDocs(LoginRequiredMixin, TemplateView):
    template_name = 'profile/emaildocs.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'docs' in self.request.GET:
            docs = models.DocsFile.objects.get(pk=self.request.GET['docs'])
            context['docs'] = docs
        return context

    def post(self, request, *args, **kwargs):
        docs = models.DocsFile.objects.get(pk=self.request.POST['docs_id'])
        file = docs.name+'.'+docs.extension
        path = os.path.join(MEDIA_ROOT, str(docs.docs))
        data = {'filename': file, 'comments': request.POST['comments']}
        mail.send(
            request.POST['email'],
            DEFAULT_FROM_EMAIL,
            template='send_docs',
            context=data,
            priority='now',
            attachments={
                file: path
            }
        )
        return HttpResponseRedirect('/mydocs')


