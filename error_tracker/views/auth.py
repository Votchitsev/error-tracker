"""Views for authentication."""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from error_tracker.forms.auth import AuthForm
from error_tracker.routes import Routes


def auth_view(request):
    """View for authentication page."""

    if request.method == "POST":
        form = AuthForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["login"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(Routes.root.value)

            return HttpResponseRedirect(Routes.auth.value)

    else:
        auth_form = AuthForm()

    return render(request, "auth.html", {"form": auth_form})
