"""Defines URL patterns for users"""

from . import views
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls')),

    # registration page
    path('register/', views.register, name='register'),
]
