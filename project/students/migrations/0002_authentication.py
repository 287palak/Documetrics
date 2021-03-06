# Generated by Django 4.0.4 on 2022-05-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='dataset_engage/test_images')),
                ('exam', models.TextField()),
            ],
        ),
    ]
