from django.shortcuts import render

# Create your views here.

def account(request):
    return render(request, 'customer/account.html')

def homepage(request):
    return render(request, 'customer/homepage.html')

def movie(request):
    return render(request, 'customer/movie_page.html')

def my_list(request):
    return render(request, 'customer/my_list.html')

def new_releases(request):
    return render(request, 'customer/new_releases.html')

def rented(request):
    return render(request, 'customer/rented.html')


