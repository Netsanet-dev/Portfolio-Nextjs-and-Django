# Generated by Django 5.1.5 on 2025-01-21 19:30

import datetime
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('contact_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=20)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Experiance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_role', models.CharField(max_length=100)),
                ('ex_company', models.CharField(blank=True, max_length=200, null=True)),
                ('ex_desc', models.TextField()),
                ('ex_start_date', models.DateField(auto_now=True)),
                ('ex_end_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homePhoto', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_date', models.DateField(auto_created=True)),
                ('project_title', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=20)),
                ('project_desc', models.CharField(max_length=200)),
                ('project_client', models.CharField(blank=True, default='personal', max_length=50, null=True)),
                ('project_edited', models.DateTimeField(default=datetime.datetime.today)),
                ('project_demo_link', models.URLField(max_length=300)),
                ('project_demo_file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_title', models.CharField(max_length=100)),
                ('serv_TechStack', models.CharField(max_length=200)),
                ('serv_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_desc', models.TextField()),
                ('skill_percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_first_name', models.CharField(max_length=10)),
                ('my_last_name', models.CharField(max_length=10)),
                ('my_phone', models.IntegerField(blank=True, null=True)),
                ('my_language', models.CharField(max_length=100)),
                ('my_desc', models.TextField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(default=datetime.datetime.today)),
                ('my_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aboutme')),
            ],
        ),
    ]
