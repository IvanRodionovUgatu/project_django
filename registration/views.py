from django import forms
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView

from .models import *


class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # перенаправление на страницу входа после успешной регистрации
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'This username is already taken.')
            return self.form_invalid(form)
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username
        return context


def logout_user(request):
    logout(request)
    return redirect('home')

