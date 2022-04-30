from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginInterfaceTemplate.as_view(), name='login'),
    path('logout', views.LogoutInterfaceTemplate.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup')
]
