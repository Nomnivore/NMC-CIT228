"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Homepage
    path("", views.index, name="index"),
    
    # Topics index
    path("topics/", views.topics, name="topics"),
    
    # Detail view for a single topic
    path("topic/<int:topic_id>/", views.topic, name="topic"),
]
