# Generated by Django 4.0.4 on 2022-05-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceRecognition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='dataset_engage/test_images')),
            ],
        ),
    ]
