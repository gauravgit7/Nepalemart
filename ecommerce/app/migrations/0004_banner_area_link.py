# Generated by Django 5.0.1 on 2024-01-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_banner_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner_area',
            name='Link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]