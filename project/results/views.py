from django.shortcuts import render
from django.http import HttpResponse
from results.forms import OTPform
from results.forms import FaceRecognitionform
from results.forms import uploadform
from results.results_code import face_testing
from results.results_code import otp_testing
from results.results_code import stu_id_testing
from teachers.teacher_registration import update_res
from django.conf import settings
from results.models import FaceRecognition
from results.models import OTP
import os

# Create your views here.


def results(request):
    print('results')
    form = FaceRecognitionform()
    if request.method == 'POST':
        print('results')
        form = FaceRecognitionform(request.POST or None, request.FILES or None)
        if form.is_valid():
            print('results')
            save = form.save(commit=True)
            # extract the image object from database
            primary_key = save.pk
            imgobj = FaceRecognition.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT,fileroot)
            #img = cv2.imread(filepath)
            # face detection
            #img_blob = cv2.dnn.blobFromImage(img, 1, (300, 300), (104, 177, 123), swapRB=False, crop=False)
            results = face_testing(filepath)
            print('results')

            return render(request,'result.html',{'form':form,'upload':True,'results':results})

    return render(request,'result.html',{'form':form,'upload':False})

def otp_result(request):
    form = OTPform()
    if request.method =='POST':
        form = OTPform(request.POST)
        if form.is_valid():
            otp=form.cleaned_data['otp']
            print(otp)
            results = otp_testing(otp)
            print(results)
            return render(request,'otp_result.html',{'form':form,'upload':True,'results':results})

    return render(request,'otp_result.html',{'form':form,'upload':False})


def result_uploading(request):
    form = uploadform()
    if request.method =='POST':
        form = uploadform(request.POST)
        if form.is_valid():
            stu_id=form.cleaned_data['stu_id']
            exam=form.cleaned_data['exam']
            result=form.cleaned_data['result']
            certificate=form.cleaned_data['certificate']
            data=stu_id_testing(stu_id)
            update_res(data['ADH_no'][0],stu_id,data['Name'][0],exam,result,certificate)
            return render(request,'upload_new.html',{'form':form,'upload':True})
    return render(request,'upload_new.html',{'form':form,'upload':False})

