# Generated by Django 4.0.3 on 2022-03-29 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_alter_tutorial_content_type_alter_tutorial_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_types', to='tutorial.contenttype'),
        ),
    ]
