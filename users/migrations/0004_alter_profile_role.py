# Generated by Django 4.2.7 on 2023-11-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default='No especificado', max_length=20),
        ),
    ]
