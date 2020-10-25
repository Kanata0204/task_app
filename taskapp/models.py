from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=140)
    time_limit = models.DateTimeField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title