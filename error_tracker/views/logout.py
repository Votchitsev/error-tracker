from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from error_tracker.routes import Routes

@login_required(login_url=Routes.auth.value)
def logout_view(request):
    """View for logout."""

    logout(request)

    return HttpResponseRedirect(Routes.root.value)
