"""
URL configuration for error_tracker project.
"""

from django.urls import include, path

from .views.logout import logout_view
from .views.errors import errors_view
from .views.auth import auth_view
from .views.main import main_view
from .views.applications import applications_view, delete_application_view
from .routes import Routes


urlpatterns = [
    path('', main_view, name='main_view'),
    path(Routes.auth.value, auth_view, name='auth'),
    path(Routes.applications.value, applications_view, name='applications'),
    path(
        f"{Routes.applications.value}<int:application_id>/delete/",
        delete_application_view, name='delete_application'
    ),
    path(Routes.errors.value, errors_view, name='errors'),
    path(Routes.logout.value, logout_view, name='logout'),

    path('api/', include('error_tracker.rest.urls')),
]
