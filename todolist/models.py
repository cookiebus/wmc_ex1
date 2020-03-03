from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-updated_at',)
    def __str__(self):
        return self.title

class Activity(models.Model):
    theme = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()

class Question(models.Model):
    title = models.CharField(max_length=255)


