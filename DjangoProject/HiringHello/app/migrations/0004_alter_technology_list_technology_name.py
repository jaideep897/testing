# Generated by Django 4.2.5 on 2023-09-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_technology_list_rename_address_companydetail_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology_list',
            name='Technology_Name',
            field=models.CharField(max_length=100 ,null=False)
        ),
    ]
