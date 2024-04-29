from django.db import models
from django.db.models import CharField


class Teacher(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)
    department = models.CharField('кафедра', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Subject(models.Model):
    name = models.CharField('Название предмета', max_length=100)
    comment = models.TextField('Комментарий к предмету', blank=True)
    deadline = models.DateTimeField('Дедлайн', blank=True)
    count_lecture = models.PositiveIntegerField('Количество лекций')
    count_seminar = models.PositiveIntegerField('количество практик')
    count_laboratory_work = models.PositiveIntegerField('Количество лаб')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='преподаватель')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> CharField:
        return self.name
