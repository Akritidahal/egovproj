# Generated by Django 3.0.2 on 2021-03-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210319_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='p_house_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='t_house_no',
            field=models.IntegerField(blank=True),
        ),
    ]
