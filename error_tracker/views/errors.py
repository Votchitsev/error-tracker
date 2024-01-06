from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from error_tracker.forms.errors import ErrorForm
from error_tracker.models import Error


@login_required(login_url="/error-tracker/auth/")
def errors_view(request):
    """View for errors."""

    if (request.method == "POST"):
        form = ErrorForm(request.POST)

        if form.is_valid():

            errors_data = (
                Error.objects.filter(
                    timestamp__date__gte=form.cleaned_data["start_date"],
                    timestamp__date__lte=form.cleaned_data["end_date"],
                    application=form.cleaned_data["application"],
                )
                .values('error_text')
                .annotate(count=Count('error_text'))
            )

        return render(request, "errors.html", {'data': errors_data, 'form': form})
    
    else:
        form = ErrorForm()

        return render(request, "get_errors.html", {'form': form})
    
