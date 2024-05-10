from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'name': 'John Doe', 'email': 'john@example.com', 'title': 'Complete Project'}
        self.task = Task.objects.create(**self.task_data)
        self.url_list = reverse('task-list')
        self.url_retrieve = reverse('task-retrieve', args=[self.task.id])
        self.url_update = reverse('task-update', args=[self.task.id])
        self.url_delete = reverse('task-delete', args=[self.task.id])

    def test_list_tasks(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_task(self):
        response = self.client.get(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'name': 'Updated Name', 'email': 'updated@example.com', 'title': 'Updated Title'}
        response = self.client.put(self.url_update, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(self.url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)