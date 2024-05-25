from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient

from core import models
from core.models import Subject


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

class SubjectAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.subject1 = Subject.objects.create(name='Subject 1', description='Description 1')
        self.subject2 = Subject.objects.create(name='Subject 2', description='Description 2')

    def test_list(self):
        response = self.client.get('/subjects_rest/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail(self):
        response = self.client.get(f'/subjects_rest/{self.subject1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Subject 1')

    def test_create(self):
        data = {'name': 'New Subject', 'description': 'New Description'}
        response = self.client.post('/subjects_rest/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subject.objects.count(), 3)

    def test_update(self):
        data = {'name': 'Updated Subject', 'description': 'Updated Description'}
        response = self.client.put(f'/subjects_rest/{self.subject1.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.subject1.refresh_from_db()
        self.assertEqual(self.subject1.name, 'Updated Subject')

    def test_partial_update(self):
        data = {'description': 'Partial Updated Description'}
        response = self.client.patch(f'/subjects_rest/{self.subject1.pk}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.subject1.refresh_from_db()
        self.assertEqual(self.subject1.description, 'Partial Updated Description')

    def test_delete(self):
        response = self.client.delete(f'/subjects_rest/{self.subject1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subject.objects.count(), 1)
