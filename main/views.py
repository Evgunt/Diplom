from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from . import models, forms


def index(request):
    return render(request, 'index.html')


class UserLogin(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next_page = '/profile'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'
    login_url = '/'
    next_page = '/'


def profile(request):
    return render(request, 'profile/profile.html')


class Registration(CreateView):
    model = models.AdvUser
    template_name = 'auth/registration.html'
    form_class = forms.RegisterUserForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            return render(request, 'auth/registration.html')
