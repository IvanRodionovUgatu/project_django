from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core import models, filters, forms, serializers


class Home(ListView):
    model = models.Subject
    context_object_name = 'subject_deadline'
    template_name = 'core/home.html'

    def get_queryset(self):
        return self.model.objects.filter(deadline__isnull=False).order_by('deadline')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = 'Главная страница'
        context['title'] = 'Главная страница'
        context['user'] = self.request.user  # Передаем текущего пользователя
        return context


class Teachers(ListView):
    template_name = 'core/teachers.html'
    model = models.Teacher
    context_object_name = 'teachers'

    def get_filters(self):
        return filters.TeacherFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список преподавателей:'
        context['text'] = 'Список преподавателей:'
        context['filters'] = self.get_filters()
        return context


class Subjects(ListView):
    template_name = 'core/subjects.html'
    model = models.Subject
    context_object_name = 'subjects'

    def get_filters(self):
        return filters.SubjectFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список предметов:'
        context['text'] = 'Список предметов:'
        context['filters'] = self.get_filters()
        return context


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


class Info(TemplateView):
    template_name = 'core/info.html'
    extra_context = {
        'title': 'О нас'
    }


class Redirect(RedirectView):
    query_string = True
    url = 'https://itcodegroup.ru/'


class SubjectRest(APIView):
    def get_object(self, pk):
        try:
            return models.Subject.objects.get(pk=pk)
        except models.Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subject = self.get_object(pk)
        serializer = serializers.SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = self.get_object(pk)
        serializer = serializers.SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherRest(ModelViewSet):
    queryset = models.Teacher.objects.all()
    filterset_class = filters.TeacherFilter
    serializer_class = serializers.TeacherSerializer

