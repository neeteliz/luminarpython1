from django.shortcuts import render
from .import forms
from employee.models import Employee

def employeepage(request):
    emp=forms.Employeedetail()
    if request.method == 'POST':
        emp = forms.Employeedetail(request.POST)
    return render(request, "employee/regemployee.html", {'emp': emp})

def display(request):
    ename=request.POST.get("ename")
    eid=request.POST.get("eid")
    esal=request.POST.get("esal")
    design=request.POST.get("design")
    ob=Employee(ename=ename,eid=eid,esal=esal,design=design)
    ob.save()
    return getEmployee(request)

def getEmployee(request):
    ob=Employee.objects.all()
    context={'ob':ob}
    return render(request,"employee/viewemloyee.html",context)
    return getSearch(request)

def getSearch(request):
    data=request.POST.get('srch')
    st=Employee.objects.filter(ename=data)
    dict={'st':st}
    return render(request,"employee/search.html",dict)
