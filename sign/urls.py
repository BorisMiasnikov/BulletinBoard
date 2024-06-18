from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from sign.views import BaseRegisterView, GetCode

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='signup.html'),
         name='signup'),
    path('logout_confirm/',
         TemplateView.as_view(template_name='logout_confirm.html'),
         name='logout_confirm'),
    path('code/<str:user>',
         GetCode.as_view(),
         name='code'),
]

