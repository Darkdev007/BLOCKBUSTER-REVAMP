from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView 
from django.contrib.auth.models import User
from .forms import UserCreationForm, RegisterForm


class LandingPageView(TemplateView):
    template_name = "pages/landing_page.html"

def sign_in(request):
    return render(request, 'pages/sign_in.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('sign-in')
    else:
        form = RegisterForm()

    return render(request, 'pages/register.html',
    {
        'form': form
    }
    )
   
