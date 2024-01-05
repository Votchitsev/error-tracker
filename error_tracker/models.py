"""Models for error_tracker app."""

from uuid import uuid4

from django.db import models


class Application(models.Model):
    """Model for application."""

    name = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid4)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Error(models.Model):
    """Model for error."""

    application = models.ForeignKey("Application", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    error_text = models.TextField()
    error_trace = models.TextField()
