# Generated by Django 3.2.6 on 2024-06-04 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='account',
            name='longitude',
        ),
    ]
