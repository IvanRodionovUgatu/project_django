from django import forms
from core import models


class SubjectForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дедлайн'
    )

    class Meta:
        model = models.Subject
        exclude = ['user']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = '__all__'
