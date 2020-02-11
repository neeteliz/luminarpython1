from django.urls import path
from formapp.views import *

urlpatterns = [
    path('formapp/',formPage,name="formapp"),
]