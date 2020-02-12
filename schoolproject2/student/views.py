from django.shortcuts import render
from .import forms
from student.models import Student

# Create your views here.
def studentpage(request):
    stud=forms.Studentname()
    if request.method == 'POST':
        stud = forms.Studentname(request.POST)
    return render(request, "student/registration.html", {'stud': stud})

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
    return render(request,"student/studentlist.html",context)