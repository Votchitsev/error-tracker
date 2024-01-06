from django import forms

from error_tracker.models import Application


class ErrorForm(forms.Form):
    """Form for error."""

    start_date = forms.DateField(
        required=True,
        label="Начальная дата",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    end_date = forms.DateField(
        required=True,
        label="Конечная дата",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    application = forms.ModelChoiceField(
        required=True,
        label="Приложение",
        queryset=Application.objects.all()
    )
