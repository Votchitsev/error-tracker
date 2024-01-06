"""Views for rest app."""

from django.http import HttpResponse
from rest_framework.decorators import api_view

from error_tracker.models import Application, Error


@api_view(["POST"])
def post_error(request):
    """View for post error endpoint."""

    application_id = Application.objects.get(token=request.data["app_token"]).id

    if application_id is not None:
        Error.objects.create(
            application_id=application_id,
            error_text=request.data["error_text"],
            error_stack=request.data["error_stack"],
        )

        return HttpResponse(status=200)
    
    return HttpResponse(status=404)
