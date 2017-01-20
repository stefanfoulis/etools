# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-12 10:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t2f', '0004_actionpoint_squashed_0014_auto_20170111_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionpoint',
            name='assigned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actionpoint',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('ongoing', 'On-going'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=254, null=True, verbose_name='Status'),
        ),
    ]