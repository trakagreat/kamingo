# Generated by Django 4.0.1 on 2022-01-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
