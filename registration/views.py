from django import forms
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, UpdateView

from .forms import *
from registration import models


class Registration(CreateView):
    model = models.Profile
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # перенаправление на страницу входа после успешной регистрации
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        # Сначала создаем пользователя
        user = form.save()

        # Затем создаем профиль для пользователя
        profile = models.Profile.objects.create(user=user)

        # Другие действия, которые вам могут понадобиться

        return super().form_valid(form)


class Login(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')

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


class Profile(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
