# Generated by Django 5.1.5 on 2025-01-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_accounts_alter_aboutme_my_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='my_phone',
            field=models.IntegerField(default=0),
        ),
    ]
