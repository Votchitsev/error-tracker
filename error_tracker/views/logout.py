from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url="/error-tracker/auth/")
def logout_view(request):
    """View for logout."""

    logout(request)

    return HttpResponseRedirect("/")
