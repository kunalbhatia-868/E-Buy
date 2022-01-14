# Generated by Django 3.2.9 on 2022-01-14 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=datetime.date(2022, 1, 18)),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
