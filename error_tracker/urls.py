"""
URL configuration for error_tracker project.
"""

from django.urls import include, path

from .views.logout import logout_view
from .views.errors import errors_view
from .views.auth import auth_view
from .views.main import main_view
from .views.applications import register_application_view, applications_view, delete_application_view

urlpatterns = [
    path('', main_view, name='main_view'),
    path('auth/', auth_view, name='auth'),
    path('register-application/', register_application_view, name='register_application'),
    path('applications/', applications_view, name='applications'),
    path('applications/<int:application_id>/delete/', delete_application_view, name='delete_application'),
    path('errors/', errors_view, name='errors'),
    path('logout', logout_view, name='logout'),

    path('api/', include('error_tracker.rest.urls')),
]
