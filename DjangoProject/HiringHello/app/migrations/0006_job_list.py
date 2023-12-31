# Generated by Django 4.2.5 on 2023-10-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_technology_list_technology_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=50)),
                ('post_date', models.DateField()),
                ('technology', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('salary_LPA', models.IntegerField()),
                ('post_name', models.CharField(max_length=300)),
                ('experience_required', models.CharField(max_length=300)),
            ],
        ),
    ]
