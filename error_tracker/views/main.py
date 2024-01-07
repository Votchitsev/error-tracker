"""Views for main page."""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from error_tracker.routes import Routes

@login_required(login_url=Routes.auth.value)
def main_view(request):
    """View for main page."""

    return HttpResponseRedirect(Routes.errors.value)
