from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
# Create your views here.


class LoginInterfaceTemplate(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceTemplate(LogoutView):
    template_name = 'home/logout.html'


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'home/signup.html'
    success_url = '/portfolio/home'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/portfolio/home')
        return super().get(self, request, *args, **kwargs)
