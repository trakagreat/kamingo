# Generated by Django 4.0.1 on 2022-01-22 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0010_alter_servicemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
