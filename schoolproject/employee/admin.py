from django.contrib import admin
from employee.models import Emp
from employee.models import Empdetail

# Register your models here.
admin.site.register(Emp)
admin.site.register(Empdetail)