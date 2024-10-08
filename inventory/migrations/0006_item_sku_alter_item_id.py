# Generated by Django 4.2.7 on 2023-12-01 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_merge_20231119_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
