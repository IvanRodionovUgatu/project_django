from django.test import TestCase, Client

from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.teacher = models.Teacher.objects.create(
            first_name='Петров',
            last_name='Александр',
        )

    def test_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


    def test_teacher(self):
        response = self.client.get(f'/teacher/{self.teacher.id}/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

