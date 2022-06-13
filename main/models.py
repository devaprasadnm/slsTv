from django.db import models

# Create your models here.

class News(models.Model):
    Title = models.CharField(max_length=100, default=None)
    Content = models.TextField()

