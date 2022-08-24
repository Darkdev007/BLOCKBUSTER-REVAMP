
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.views.generic import TemplateView 
from django.contrib.auth.models import User
from .forms import UserCreationForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate


class LandingPageView(TemplateView):
    template_name = "pages/landing_page.html"



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = RegisterForm()

    return render(request, 'pages/register.html',
    {
        'form': form
    }
    )
   
def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('homepage')
            else:
                messages.error(request, 'Username or password is not correct')
                return redirect('sign_in')
    else:
        login_form = LoginForm()

    return render(request, 'pages/sign_in.html',
    {
        'login_form' : login_form
    }
    )