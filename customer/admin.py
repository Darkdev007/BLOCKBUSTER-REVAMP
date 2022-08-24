from django.contrib import admin
from .models import LocalMovies, ForeignMovies, Rented

# Register your models here.

admin.site.register(LocalMovies)
admin.site.register(ForeignMovies)
admin.site.register(Rented)