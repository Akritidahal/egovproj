# Generated by Django 3.0.2 on 2021-03-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citizen',
            old_name='grand_father_name',
            new_name='grandfather_name',
        ),
        migrations.RenameField(
            model_name='citizen',
            old_name='p_ward_no',
            new_name='p_ward',
        ),
        migrations.RenameField(
            model_name='citizen',
            old_name='t_ward_no',
            new_name='t_ward',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='photo',
        ),
        migrations.AddField(
            model_name='citizen',
            name='birth_certificate_photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='father_citizenship_photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='husband_citizen_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='citizen',
            name='husband_citizenship_photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='husband_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='citizen',
            name='mother_citizen_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='citizen',
            name='mother_citizenship_photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='mother_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='father_citizen_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='father_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]