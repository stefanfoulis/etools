# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-29 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20161227_1953'),
        ('partners', '0007_auto_20161229_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='country_programme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agreements', to='reports.CountryProgramme'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='status',
            field=django_fsm.FSMField(blank=True, choices=[(b'draft', b'Draft'), (b'cancelled', b'Cancelled'), (b'active', b'Active'), (b'ended', b'Ended'), (b'suspended', b'Suspended'), (b'terminated', b'Terminated')], default=b'draft', max_length=32),
        ),
    ]