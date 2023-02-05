from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from . import models, forms, utilities


def index(request):
    return render(request, 'index.html')


class UserLogin(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next_page = '/profile'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'
    login_url = '/login'
    next_page = '/'


class Registration(CreateView):
    model = models.AdvUser
    template_name = 'auth/registration.html'
    form_class = forms.RegisterUserForm
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            return render(request, 'auth/registration.html')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = models.AdvUser.objects.get(pk=self.request.user.pk)
        user = utilities.decode(user)
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
    success_url = '/profile'
    login_url = '/login'
    pk_url_kwarg = id

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        user = get_object_or_404(queryset, pk=pk)
        user = utilities.decode(user)
        return user


class ChangePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profile/changePass.html'
    success_url = '/profile'
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = models.AdvUser.objects.get(pk=request.user.pk)
            newUser = utilities.decode(user)
            newUser.set_password(request.POST['new_password1'])
            newUser = utilities.encode(newUser)
            newUser.save()
        return render(request, 'profile/changePass.html')


def fogot_password_form(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        context = {'display': 'none'}
        if request.method == "POST":
            username = request.POST['username']
            if models.AdvUser.objects.filter(username=username).exists():
                user = models.AdvUser.objects.get(username=username)
                utilities.send_password_notification(user)
                context['mail'] = "Проверьте почту"
                context['display'] = 'block'
            else:
                context['errors'] = "Введен неверный логин"
        return render(request, 'auth/password_email_form.html', context)


def password_email(request, sign):
    username = utilities.signer.unsign(sign)
    user = get_object_or_404(models.AdvUser, username=username)
    password = utilities.generate_password()
    user.set_password(password)
    user.save()
    context = {'user': username, 'password': password}
    return render(request, 'auth/password_change_email.html', context)

