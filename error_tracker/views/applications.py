"""Views for applications."""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from error_tracker.forms.register_application import RegisterApplicationForm
from error_tracker.models import Application
from error_tracker.routes import Routes


@login_required(login_url=Routes.auth.value)
def applications_view(request):
    """View for applications page."""

    applications = Application.objects.filter(user_id=request.user)

    if request.method == "POST":
        form = RegisterApplicationForm(request.POST)

        if form.is_valid():
            application = Application(
                name=form.cleaned_data["name"],
                user = request.user,
            )

            application.save()

            return render(request, "applications.html", {"applications": applications, "form": form})

    else:
        form = RegisterApplicationForm()

    return render(request, "applications.html", {"applications": applications, "form": form})


@login_required(login_url=Routes.auth.value)
def delete_application_view(request, application_id):
    """View for delete application."""

    application = Application.objects.get(id=application_id)

    application.delete()

    return HttpResponseRedirect(f"/{Routes.applications.value}")
