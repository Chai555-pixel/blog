# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page for blog
    path('about/', views.about, name='about'),  # About page for blog
]
