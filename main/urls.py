from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.UserLogin.as_view(), name='login'),
   path('logout', views.Logout.as_view(), name='Logout'),
   path('profile', views.profile, name='profile'),
]
