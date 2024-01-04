"""Form for authentication."""
from django import forms

class AuthForm(forms.Form):
    """Form for authentication."""

    login = forms.CharField(required=True, label="Логин")
    password = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput)
