from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from student.views import *

urlpatterns = [
    path('registration/',register,name="studreg"),
    path('studentlist',display,name='studlist'),
    path('viewstudent',getStudent,name='viewlist'),

]
