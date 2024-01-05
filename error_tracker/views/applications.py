"""Views for applications."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from error_tracker.forms.register_application import RegisterApplicationForm
from error_tracker.models import Application


@login_required(login_url="/error-tracker/auth/")
def register_application_view(request):
    """View for register application."""

    if request.method == "POST":
        form = RegisterApplicationForm(request.POST)

        if form.is_valid():
            application = Application(
                name=form.cleaned_data["name"],
                user = request.user,
            )

            application.save()

            return render(
                request,
                "register_application_success.html",
                {
                    "name": application.name,
                    "application_token": application.token,
                },
            )

    else:
        form = RegisterApplicationForm()

    return render(request, "register_application.html", {"form": form})


@login_required(login_url="/error-tracker/auth/")
def applications_view(request):
    """View for applications page."""

    applications = Application.objects.filter(user_id=request.user)

    return render(request, "applications.html", {"applications": applications})


@login_required(login_url="/error-tracker/auth/")
def delete_application_view(request, application_id):
    """View for delete application."""

    application = Application.objects.get(id=application_id)

    application.delete()

    return render(request, "delete_application_success.html", {"name": application.name})
