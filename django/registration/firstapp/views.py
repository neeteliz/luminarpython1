from django.shortcuts import render

# Create your views here.
def getpage(request):
    return render(request,"firstappp/login.html")