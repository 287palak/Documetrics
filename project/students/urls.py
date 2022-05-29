from django.urls import path
from students import views

urlpatterns = [
    path('',views.student_registration,name='student_registration')
    path('auth',views.student_authentication,name='student_authentication')
]
