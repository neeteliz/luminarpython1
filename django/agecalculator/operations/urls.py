from django.contrib import admin
from django.urls import path
from operations.views import *

urlpatterns = [
    path('date/', getdate, name='datebirth'),
    path('age',printdate,name='currentage'),
]
