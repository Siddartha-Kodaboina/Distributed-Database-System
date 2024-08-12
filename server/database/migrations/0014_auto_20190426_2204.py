# Generated by Django 2.1.7 on 2019-04-26 22:04

import database.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20190426_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendingupdates',
            name='data_boolean_keys',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=database.models.PendingUpdates.default_string_array, size=None),
        ),
        migrations.AddField(
            model_name='pendingupdates',
            name='data_boolean_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), default=database.models.PendingUpdates.default_string_array, size=None),
        ),
    ]
