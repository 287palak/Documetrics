"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from results import views
from teachers import views as views_teach
from students import views as views_stu
from project import views as vw
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',vw.home,name="home"),
    path('admin', admin.site.urls),
    path('results',views.results,name='results'),
    path('options',vw.options,name='options'),
    path('options_stu',vw.options_stu,name='options_stu'),
    path('student_registration',views_stu.student_registration,name='student_registration'),
    path('teachers_registration',views_teach.teacher_registration,name='teacher_registration'),
    path('student_authentication',views_stu.student_authentication,name='student_authentication'),
    path('teacher_authentication',views_teach.teacher_authentication,name='teacher_authentication'),
    path('otp_result',views.otp_result,name='otp_results'),
    path('biometrics',vw.biometrics,name='biometrics'),
    path('biometrics_stu',vw.biometrics_stu,name='biometrics_stu'),
    path('mobile_otp',vw.mobile_otp,name='mobile_otp'),
    path('upload',views.result_uploading,name='upload'),
    path('mobile_post_otp',vw.mobile_post_otp,name='post_reg_mobile_otp')
    ]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

