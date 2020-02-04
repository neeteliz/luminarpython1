from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"students/registration.html")

def printdata(request):
    name = request.POST.get("fname")
    age = request.POST.get("age")
    phno = request.POST.get("phn")
    context= {"name":name+age+phno}
    return render(request,'students/studenthome.html',context)