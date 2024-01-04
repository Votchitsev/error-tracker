"""Views for authentication."""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


from error_tracker.forms.auth import AuthForm

def auth_view(request: object) -> object:
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
                return HttpResponseRedirect("/error-tracker/")

            return HttpResponseRedirect("/error-tracker/auth/")

    else:
        auth_form = AuthForm()

    return render(request, "auth.html", {"form": auth_form})
