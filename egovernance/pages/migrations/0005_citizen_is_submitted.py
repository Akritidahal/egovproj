# Generated by Django 3.1.7 on 2021-03-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_citizen_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
