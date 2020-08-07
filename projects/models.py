from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100)
    technology = models.CharField(max_length=60)
    image = models.FilePathField(path='/img')

# Create your models here.
