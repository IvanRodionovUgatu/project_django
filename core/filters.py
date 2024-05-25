import django_filters
from django.db.models import Q

from core.models import Subject, Teacher


class SubjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название', lookup_expr='icontains')
    deadline_to = django_filters.DateFilter(field_name='deadline', lookup_expr='lt', label='Дедлайн по')
    count_lecture_from = django_filters.NumberFilter(field_name='count_lecture', lookup_expr='gt',
                                                     label='Количество лекций от')

    class Meta:
        model = Subject
        fields = '__all__'
        exclude = ['comment']


class TeacherFilter(django_filters.FilterSet):
    fio = django_filters.CharFilter(method='filter_fio', label='Фамилия и имя')

    class Meta:
        model = Teacher
        exclude = ['photo']

    def filter_fio(self, queryset, name, value):
        return queryset.filter(Q(first_name__icontains=value) | Q(last_name__icontains=value))
