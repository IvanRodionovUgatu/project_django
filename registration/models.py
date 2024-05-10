from django.db import models


class User(models.Model):
    nickname = models.CharField('Никнейм', max_length=30)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    email = models.EmailField('Почта', blank=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    is_active = models.BooleanField('Активен', default=True)
    date_joined = models.DateTimeField('Дата', auto_now_add=True)
    is_verified = models.BooleanField('Верифицирован', default=False)
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
