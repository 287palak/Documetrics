# Generated by Django 4.0.4 on 2022-05-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_authentication_teacher_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication_teacher',
            name='image',
            field=models.ImageField(upload_to='dataset_engage/test_images'),
        ),
        migrations.AlterField(
            model_name='registration_teacher',
            name='image',
            field=models.ImageField(upload_to='dataset_engage/test_images'),
        ),
    ]
