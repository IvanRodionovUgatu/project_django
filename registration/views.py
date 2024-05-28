from django import forms
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, CreateView, TemplateView, UpdateView, DetailView, ListView, DeleteView

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


class ProfileEdit(UpdateView):
    model = models.Profile
    form_class = ProfileForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile


class Profile(DetailView):
    model = models.Profile
    template_name = 'registration/profile.html'

    def get_object(self, queryset=None):
        # Возвращаем профиль текущего пользователя
        return models.Profile.objects.get(user=self.request.user)


class SendMessage(CreateView):
    form_class = SendMessageForm
    template_name = 'registration/send_message.html'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.sender = self.request.user
        form.instance.recipient = User.objects.get(pk=pk)

        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.recipient.id
        return reverse('message_list', kwargs={'pk': pk})


class MessageList(ListView):
    model = models.Message
    template_name = 'registration/message_list.html'
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        recipient_id = get_object_or_404(User, id=pk)
        context['recipient_id'] = recipient_id.id
        return context

    def get_queryset(self):
        pk = self.kwargs['pk']
        recipient = get_object_or_404(User, id=pk)
        user = self.request.user
        return models.Message.objects.filter(
            (Q(sender=user) & Q(recipient=recipient)) |
            (Q(sender=recipient) & Q(recipient=user))
        ).order_by('timestamp')


class UserList(ListView):
    model = models.User
    template_name = 'registration/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id).select_related('profile')


class MessageDeleteView(DeleteView):
    model = models.Message
    template_name = 'registration/message_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # В контексте передаем идентификатор получателя и отправителя
        context['recipient_id'] = self.object.recipient.id
        return context

    def get_success_url(self):
        message = self.get_object()

        if self.request.user == message.sender:
            # Если текущий пользователь - отправитель сообщения, перенаправляем на страницу получателя
            return reverse('message_list', kwargs={'pk': message.recipient.id})
        else:
            # Если текущий пользователь - получатель сообщения, перенаправляем на страницу отправителя
            return reverse('message_list', kwargs={'pk': message.sender.id})
