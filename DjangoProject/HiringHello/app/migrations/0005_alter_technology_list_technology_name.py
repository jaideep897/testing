# Generated by Django 4.2.5 on 2023-09-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_technology_list_technology_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology_list',
            name='Technology_Name',
            field=models.CharField( max_length=100),
        ),
    ]