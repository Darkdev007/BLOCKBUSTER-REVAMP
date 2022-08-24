
from shutil import _ntuple_diskusage
from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField

# Create your models here.

class ForeignMovies(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'foreign_images')
    newly_released = models.BooleanField(default=True)
    description = models.TextField(max_length=300)
    video = models.FileField(upload_to='foreign_videos')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name_plural = 'Foreign Movies'

class LocalMovies(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'local_images')
    newly_released = models.BooleanField(default=True)
    description = models.TextField(max_length=300)
    video = models.FileField(upload_to='local_videos')
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name_plural = 'Local Movies'


class Rented(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    foreign_movies = models.ManyToManyField(ForeignMovies)
    local_movies = models.ManyToManyField(LocalMovies)

    class Meta:
        verbose_name_plural = 'Rented'

