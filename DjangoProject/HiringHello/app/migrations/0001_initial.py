# Generated by Django 4.2.5 on 2023-09-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companydetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=300)),
                ('source', models.CharField(max_length=300)),
                ('City', models.CharField(max_length=500)),
                ('Address', models.CharField(max_length=500)),
                ('Website', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='companymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('DOB', models.DateField()),
                ('CompanyName', models.CharField(max_length=500)),
                ('currentposition', models.CharField(max_length=300)),
                ('Experience', models.CharField(max_length=300)),
                ('CTC', models.IntegerField()),
                ('ECTC', models.IntegerField()),
                ('Notice', models.CharField(max_length=400)),
                ('JobLocation', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('CommunicationRating', models.CharField(max_length=100)),
                ('CV', models.FileField(upload_to='uploads/')),
                ('Feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]