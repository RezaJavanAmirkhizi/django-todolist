from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager



class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'L', 'Low'
        Medium = 'M', 'Medium'
        High = 'H', 'High'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    priority = models.CharField(
        max_length=1, choices=Priority.choices, default=Priority.LOW)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title
