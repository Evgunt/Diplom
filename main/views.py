from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')


class UserLogin(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = '/profile'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    login_url = '/'
    next_page = '/'


def profile(request):
    return render(request, 'profile/profile.html')
