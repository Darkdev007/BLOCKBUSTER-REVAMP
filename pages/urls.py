from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view() , name='landing_page'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('register', views.register, name="register"),    
]
