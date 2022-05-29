from django.db import models


# Create your models here.
class FaceRecognition(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'dataset_engage/test_images')


    def __str__(self):
        return str(self.record_date)

class OTP(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField()

    def __str__(self):
        return str(self.record_date)

class upload(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    stu_id = models.IntegerField()
    exam = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    certificate = models.IntegerField()

    def __str__(self):
        return str(self.record_date)