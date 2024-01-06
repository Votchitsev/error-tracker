"""urls for rest app."""

from django.urls import path

from .views import post_error


urlpatterns = [
    path('', post_error, name='post_error'),
]
