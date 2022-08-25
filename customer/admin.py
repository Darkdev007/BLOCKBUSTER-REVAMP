from django.contrib import admin
from .models import LocalMovies, ForeignMovies, Rented

# Register your models here.
class LocalMoviesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = { 'slug' : ('title',)}

class ForeignMoviesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(LocalMovies, LocalMoviesAdmin)
admin.site.register(ForeignMovies, ForeignMoviesAdmin)
admin.site.register(Rented)