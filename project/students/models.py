from django.db import models


# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    image = models.ImageField(upload_to = 'dataset_engage/test_images')
    exam = models.TextField()

    def __str__(self):
        return str(self.record_date)

class Registration_teacher(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    image = models.ImageField(upload_to='dataset_engage/test_images')
    exam = models.TextField()

    def __str__(self):
        return str(self.record_date)

class Authentication(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    image = models.ImageField(upload_to = 'dataset_engage/test_images')
    exam = models.TextField()

    def __str__(self):
        return str(self.record_date)