# Generated by Django 4.2.5 on 2023-10-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_job_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_list',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
