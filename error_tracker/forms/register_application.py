from django import forms


class RegisterApplicationForm(forms.Form):
    """Form for registration application."""

    name = forms.CharField(required=True, max_length=255, label="Название приложения")
