# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-02-11 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_tshirts'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='other_gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('NA', 'Prefer not to answer'), ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary'), ('X', 'Prefer to self-describe')], default='NA', max_length=23),
        ),
    ]