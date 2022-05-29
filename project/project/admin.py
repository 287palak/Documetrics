from django.contrib import admin
from results.models import FaceRecognition
from students.models import Registration
# Register your models here.

admin.site.register(FaceRecognition)
admin.site.register(Registration)
