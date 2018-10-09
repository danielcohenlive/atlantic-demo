# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('street_address', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('new', 'new'), ('canceled', 'canceled')], max_length=8)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.Product')),
            ],
        ),
    ]