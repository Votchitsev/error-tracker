"""Views for main page."""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/error-tracker/auth/")
def main_view(request):
    """View for main page."""

    return HttpResponseRedirect("/error-tracker/errors/")
