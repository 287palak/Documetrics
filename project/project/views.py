from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "../templates/index_new.html")

def teachers_registration(request):
    return render(request, "../templates/teacher_reg_temp.html")

def teacher_authentication(request):
    return render (request, "../templates/teacher_authentication.html")

def results(request):
    return render (request, "../templates/result.html")

def otp_result(request):
    return render(request, "../templates/otp_result.html")

def options(request):
    return render(request, "../templates/options.html")

def options_stu(request):
    return render(request, "../templates/options_stu.html")

def biometrics(request):
    return render(request, "../templates/biometrics.html")

def mobile_otp(request):
    return render(request, "../templates/mobile_otp.html")

def biometrics_stu(request):
    return render(request, "../templates/biometrics_stu.html")

def upload_res(request):
    return render(request, "../templates/upload_new.html")

def mobile_post_otp(request):
    return render(request, "../templates/post_reg_mobile_otp.html")