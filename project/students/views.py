from django.shortcuts import render
from django.http import HttpResponse
from students.forms import Registrationform
from students.forms import Authenticationform
from students.student_registration import student_register
from students.student_registration import student_authentication as student_authentication2
from django.conf import settings
from students.models import Registration
from students.models import Authentication
import os 

# Create your views here.
def student_registration(request):
    form = Registrationform()

    if request.method == 'POST':
        form = Registrationform(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)

            # extract the image object from database
            primary_key = save.pk
            imgobj = Registration.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            name = str(imgobj.name)
            exam =str(imgobj.exam)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            data = student_register(name, filepath, exam)
            print(data)
            return render(request,'student_reg.html',{'form':form,'upload':True,'results':data})

    return render(request,'student_reg.html',{'form':form,'upload':False})


def student_authentication(request):
    form2 = Authenticationform()
    if request.method == 'POST':
        form2 = Authenticationform(request.POST or None, request.FILES or None)
        if form2.is_valid():
            save = form2.save(commit=True)

            # extract the image object from database
            primary_key = save.pk
            imgobj = Authentication.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            name = str(imgobj.name)
            exam =str(imgobj.exam)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            data = student_authentication2(name, filepath, exam)
            print(data)

            return render(request,'student_auth.html',{'form':form2,'upload':True,'results':data})

    return render(request,'student_auth.html',{'form':form2,'upload':False})

