# Generated by Django 4.0.4 on 2022-05-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_authentication_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication_teacher',
            name='image',
            field=models.ImageField(upload_to='../media/dataset_engage/test_images'),
        ),
        migrations.AlterField(
            model_name='registration_teacher',
            name='image',
            field=models.ImageField(upload_to='../media/dataset_engage/test_images'),
        ),
    ]
