from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.UserLogin.as_view(), name='login'),
   path('logout', views.Logout.as_view(), name='logout'),
   path('profile/', views.Profile.as_view(), name='profile'),
   path('changeprofile/<int:pk>', views.ChangeUser.as_view(), name='changeprofile'),
   path('registration', views.Registration.as_view(), name='Registration'),
   path('changepass/<int:pk>', views.ChangePass.as_view(), name='changepass'),
]
