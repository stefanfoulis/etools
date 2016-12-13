# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-09 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('et2f', '0007_auto_20161201_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelactivity',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='travelactivity',
            name='partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='partners.PartnerOrganization'),
        ),
        migrations.AlterField(
            model_name='travelactivity',
            name='partnership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='partners.PCA'),
        ),
        migrations.AlterField(
            model_name='travelactivity',
            name='result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reports.Result'),
        ),
    ]