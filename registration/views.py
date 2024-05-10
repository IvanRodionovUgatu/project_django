from django import forms
from django.views.generic import FormView

from .forms import RegistrationForm
from .models import User


class Registration(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = 'login/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

