# Generated by Django 4.0.1 on 2022-01-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0005_servicemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_photos'),
        ),
    ]