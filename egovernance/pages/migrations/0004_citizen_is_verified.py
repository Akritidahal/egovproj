# Generated by Django 3.0.2 on 2021-03-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210320_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
