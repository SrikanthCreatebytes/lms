# Generated by Django 4.0.3 on 2022-03-29 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('user_role', models.CharField(choices=[('user', 'USER'), ('admin', 'ADMIN')], max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
