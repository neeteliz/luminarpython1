from django.shortcuts import render
from student.models import Student

# Create your views here.
def register(request):
    return render(request,"students/registration.html")

def display(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    crse = request.POST.get("crse")
    ob=Student(name=name,age=age,crse=crse)
    ob.save()
    return getStudent(request)

def getStudent(request):
    ob=Student.objects.all()
    context={'ob':ob}
    return render(request,"students/studentlist.html",context)