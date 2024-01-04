"""
URL configuration for error_tracker project.
"""

from django.urls import path
from .views.auth import auth_view
from .views.main import main_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('auth/', auth_view, name='auth'),
]
