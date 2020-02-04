from django.contrib import admin
from django.urls import path
from student.views import *

urlpatterns = [
    path('registration/',register,name='register'),
    path('viewdata',printdata,name='printval'),
]
