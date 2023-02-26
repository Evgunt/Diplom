from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.UserLogin.as_view(), name='login'),
   path('logout', views.Logout.as_view(), name='logout'),
   path('profile', views.Profile.as_view(), name='profile'),
   path('changeprofile/<int:pk>', views.ChangeUser.as_view(), name='changeprofile'),
   path('registration', views.Registration.as_view(), name='registration'),
   path('userprofile/<int:pk>', views.ProfileDetail.as_view(), name='userprofile'),
   path('changepass/<int:pk>', views.ChangePass.as_view(), name='changepass'),
   path('mydocs', views.MyDocs.as_view(), name='mydocs'),
   path('publicdocs', views.PublicDocs.as_view(), name='publicdocs'),
   path('docsadd', views.DocsAdd.as_view(), name='docsadd'),
   path('docsdel/<int:pk>', views.DocsDelete.as_view(), name='docsdel'),
   path('docsedit/<int:pk>', views.DocsEdit.as_view(), name='docsedit'),
   path('search', views.Search.as_view(), name='search'),
   path('email', views.EmailDocs.as_view(), name='email'),
]
