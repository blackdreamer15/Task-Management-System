from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task, related_name='categories')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task, related_name='tags')

    def __str__(self):
        return self.name
