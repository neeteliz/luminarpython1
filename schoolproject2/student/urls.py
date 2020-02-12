from django.urls import path
from student.views import *

urlpatterns = [
    path('register/',studentpage,name="studreg"),
    path('studentlist',display,name='studlist'),
    path('viewstudent',getStudent,name='viewlist'),
]