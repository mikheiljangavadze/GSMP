# Generated by Django 5.0.7 on 2025-02-12 09:27

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_alter_gsmpmember_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsmpmember',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='country'),
        ),
    ]
