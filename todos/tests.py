from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tag, Task

class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        # Create a task
        test_task = Task.objects.create(
            title='Task title', description='Body content...')
        test_task.save()

    def test_blog_content(self):
        task = Task.objects.get(id=1)
        expected_title = f'{task.title}'
        expected_description = f'{task.description}'
        self.assertEqual(expected_title, 'Task title')
        self.assertEqual(expected_description, 'Body content...')