from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ForeignMovies(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'foreign_images')
    newly_released = models.BooleanField(default=True)
    description = models.TextField(max_length=300)
    video = models.FileField(upload_to='foreign_videos')

class LocalMovies(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'local_images')
    newly_released = models.BooleanField(default=True)
    description = models.TextField(max_length=300)
    video = models.FileField(upload_to='local_videos')




