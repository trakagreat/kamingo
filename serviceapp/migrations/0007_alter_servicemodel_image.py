# Generated by Django 4.0.1 on 2022-01-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0006_alter_servicemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='image',
            field=models.ImageField(default='uploads/service_photos/123.jpg', upload_to='service_photos'),
        ),
    ]
