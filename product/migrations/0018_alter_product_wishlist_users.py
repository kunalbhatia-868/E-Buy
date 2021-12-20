# Generated by Django 3.2.9 on 2021-12-09 07:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0017_auto_20211209_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='wishlist_products', to=settings.AUTH_USER_MODEL),
        ),
    ]