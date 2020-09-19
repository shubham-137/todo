from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=12, default=" ")