# Generated by Django 4.2.5 on 2023-09-19 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetail',
            old_name='Website',
            new_name='website',
        ),
    ]