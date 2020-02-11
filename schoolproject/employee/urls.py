from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from employee.views import *

urlpatterns = [
    path('regemployee/',register,name="empreg"),
    path('employeelist/',display,name='emplist'),
    path('viewemployee/',getEmployee,name='viewemp'),
    path('search',getSearch,name='search'),

]
