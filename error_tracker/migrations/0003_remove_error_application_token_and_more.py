# Generated by Django 5.0.1 on 2024-01-05 11:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('error_tracker', '0002_alter_error_application_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='error',
            name='application_token',
        ),
        migrations.AlterField(
            model_name='application',
            name='token',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
