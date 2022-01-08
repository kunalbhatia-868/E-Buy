# Generated by Django 3.2.9 on 2022-01-08 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20220108_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery_days',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.date(2022, 1, 12)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateField(verbose_name=datetime.date(2022, 1, 8)),
        ),
    ]
