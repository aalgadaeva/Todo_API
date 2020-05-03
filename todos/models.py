from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS_CHOICES = {
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Done'),
    }

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.IntegerField(choices=STATUS_CHOICES)
    creation_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')
    
    def __str__(self):
        return self.title

