from django.shortcuts import render
from django.http import HttpResponse
from teachers.forms import Registrationform
from teachers.forms import Authenticationform
from teachers.teacher_registration import teacher_register
from teachers.teacher_registration import teacher_authentication as teacher_authentication2
from django.conf import settings
from students.models import Registration
from students.models import Authentication
import os


# Create your views here.
def teacher_registration(request):
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
            data = teacher_register(name, filepath, exam)
            print(data)
            return render(request,'teacher_reg_temp.html',{'form':form,'upload':True,'results':data})
    return render(request,'teacher_reg_temp.html',{'form':form,'upload':False})

def teacher_authentication(request):
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
            #data = teacher_authentication2(name, filepath, exam)
            #print(data)
            access = teacher_authentication2(name, filepath, exam)
            if access==0:
                return render(request, 'teacher_reg_temp.html', {'form': form2, 'upload': True, 'results': access})
            elif access==1:
                return render(request, 'post_login_teacher.html',{'form':form2, 'upload':True, 'results':access})
            else:
                return render(request,'teacher_auth.html',{'form':form2,'upload':True,'results':access})

    return render(request,'teacher_auth.html',{'form':form2,'upload':False})

