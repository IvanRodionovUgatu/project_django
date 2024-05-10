from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from core import models


class Home(ListView):
    model = models.Subject
    context_object_name = 'subject_deadline'
    template_name = 'core/home.html'
    extra_context = {
        'text': 'Главная страница',
        'title': 'Главная страница',
    }
    def get_queryset(self):
        return self.model.objects.filter(deadline__isnull=False).order_by('deadline')

class Teachers(ListView):
    template_name = 'core/teachers.html'
    model = models.Teacher
    context_object_name = 'teachers'
    extra_context = {
        'text': 'Список преподавателей:',
        'title': 'Список преподавателей',
    }


class Subjects(ListView):
    template_name = 'core/subjects.html'
    model = models.Subject
    context_object_name = 'subjects'
    extra_context = {
        'text': 'Список предметов:',
        'title': 'Список предметов',
    }


class Teacher(DetailView):
    template_name = 'core/teacher.html'
    model = models.Teacher
    pk_url_kwarg = 'id'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()
        photo = teacher.photo
        context['photo'] = photo
        context['title'] = f'{teacher.first_name} {teacher.last_name}'
        return context
