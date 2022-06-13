from django.db import models

# Create your models here.

class News(models.Model):
    Title = models.CharField(max_length=100, default=None)
    Content = models.TextField()
class Images(models.Model):
    Photos = models.ImageField(upload_to ='files')
