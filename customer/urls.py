from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('my_list', views.my_list),
    path('new_releases', views.new_releases),
    path('rented', views.rented),
    path('account', views.account),
    path('<slug:slug>', views.movie, name='movie'),

]