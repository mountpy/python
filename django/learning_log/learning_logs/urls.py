""" Define URL patterns for learning_logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path("", views.index, name='index'),
    # Page to show all Topics
    path('topics/', views.topics, name='topics'),
    # Detailed page for single topic.
    path('topic/<int:topic_id>/', views.topic, name='topic'),
] 


