# Generated by Django 5.2 on 2025-04-07 02:15

import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='password')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
