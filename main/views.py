import os

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from . import models, forms

#
# def index(request):
#     return render(request, 'index.html')


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
    success_url = '/'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = models.AdvUser.objects.get(pk=self.request.user.pk)
        # user = utilities.decode(user)
        user.dateBorn = self.dateFormat(user.dateBorn)
        context['info'] = user
        return context

    def dateFormat(self, date):
        newdate = date.split('-')
        new = newdate[2]+'.'+newdate[1]+'.'+newdate[0]
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
        # user = utilities.decode(user)
        return user


class ChangePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/changePass.html'
    success_url = '/mydocs'
    login_url = '/'


class MyDocs(LoginRequiredMixin, TemplateView):
    template_name = 'profile/mydocs.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if models.DocsFile.objects.filter(owner=self.request.user.username).exists():
            userDocs = ''
            if self.request.GET:
                if self.request.GET['filter']=='name':
                    userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('name')
                elif self.request.GET['filter']=='old':
                    userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('pk')
            else:
                userDocs = models.DocsFile.objects.filter(owner=self.request.user.username).order_by('-pk')
            context['info'] = userDocs
        return context


class PublicDocs(LoginRequiredMixin, TemplateView):
    template_name = 'profile/publicdocs.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if models.DocsFile.objects.filter(status=True).exists():
            userDocs = ''
            if self.request.GET:
                if self.request.GET['filter']=='name':
                    userDocs = models.DocsFile.objects.filter(status=True).order_by('name')
                elif self.request.GET['filter']=='old':
                    userDocs = models.DocsFile.objects.filter(status=True).order_by('pk')
            else:
                userDocs = models.DocsFile.objects.filter(status=True).order_by('-pk')
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