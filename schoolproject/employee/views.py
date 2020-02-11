from django.shortcuts import render
from employee.models import Emp
from employee.models import Empdetail

# Create your views here.
def register(request):
    return render(request,"employee/regemployee.html")

def display(request):
    eid = request.POST.get("eid")
    ename = request.POST.get("ename")
    ob=Emp(eid=eid,ename=ename)
    ob.save()
    return getEmployee(request)

def getEmployee(request):
    ob=Emp.objects.all()
    context={'ob':ob}
    return render(request,"employee/viewemployee.html",context)
    return getSearch(request)
def getSearch(request):
    data=request.POST.get('srch')
    print("dcaaaaaa",data)
    st=Emp.objects.filter(ename=data)
    emp=Emp.objects.all()
    for e in emp:
        print(e.ename)
    print(st)
    dict={'st':st}
    return render(request,"employee/search.html",dict)

