# Generated by Django 3.0.5 on 2020-05-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0011_auto_20200506_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
