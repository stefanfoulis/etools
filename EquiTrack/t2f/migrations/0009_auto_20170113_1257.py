# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-13 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publics', '0001_initial'),
        ('t2f', '0008_auto_20170113_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costassignment',
            old_name='new_fund',
            new_name='fund',
        ),
        migrations.RenameField(
            model_name='costassignment',
            old_name='new_grant',
            new_name='grant',
        ),
        migrations.RenameField(
            model_name='costassignment',
            old_name='new_wbs',
            new_name='wbs',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='new_account_currency',
            new_name='account_currency',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='new_document_currency',
            new_name='document_currency',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='new_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='new_currency',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='new_fund',
            new_name='fund',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='new_grant',
            new_name='grant',
        ),
        migrations.RenameField(
            model_name='invoiceitem',
            old_name='new_wbs',
            new_name='wbs',
        ),
        migrations.RenameField(
            model_name='iteneraryitem',
            old_name='new_dsa_region',
            new_name='dsa_region',
        ),
        migrations.RenameField(
            model_name='iteneraryitem',
            old_name='new_mode_of_travel',
            new_name='mode_of_travel',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='new_currency',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='new_mode_of_travel',
            new_name='mode_of_travel',
        ),
        migrations.AddField(
            model_name='iteneraryitem',
            name='airlines',
            field=models.ManyToManyField(related_name='_iteneraryitem_airlines_+', to='publics.AirlineCompany'),
        ),
        migrations.RenameField(
            model_name='travelactivity',
            old_name='new_travel_type',
            new_name='travel_type',
        ),
    ]