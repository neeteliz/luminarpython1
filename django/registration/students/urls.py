from django.contrib import admin
from django.urls import path,include
from students.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',studentviewss),
]