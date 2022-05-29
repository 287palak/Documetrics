from django.urls import path
from results import views

urlpatterns = [
    path('',views.results,name='results')
]
