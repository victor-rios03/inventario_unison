# Generated by Django 4.2.7 on 2023-12-01 00:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_item_sku_alter_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
