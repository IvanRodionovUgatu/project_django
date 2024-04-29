from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from core import models


class Home(TemplateView):
    template_name = 'core/home.html'
    extra_context = {
        'text': 'Главная страница',
        'title': 'Главная страница',
    }


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
