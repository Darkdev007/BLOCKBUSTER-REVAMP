from django.shortcuts import render
from .models import ForeignMovies

# Create your views here.

def account(request):
    return render(request, 'customer/account.html')

def homepage(request):
    fmovies = ForeignMovies.objects.all()[:5]
    fnmovies = ForeignMovies.objects.filter(newly_released = True)[:5]
    return render(request, 'customer/homepage.html',
    {
        'fmovies':fmovies,
        'fnmovies':fnmovies,
    }
    )

def movie(request):
    return render(request, 'customer/movie_page.html')

def my_list(request):
    return render(request, 'customer/my_list.html')

def new_releases(request):
    return render(request, 'customer/new_releases.html')

def rented(request):
    return render(request, 'customer/rented.html')


