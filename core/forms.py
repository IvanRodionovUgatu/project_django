from django import forms
from core import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = '__all__'
