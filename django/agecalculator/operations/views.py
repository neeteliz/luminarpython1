from django.shortcuts import render
from datetime import date

# Create your views here.
def getdate(request):
    return render(request,'age/agecalc.html')

def printdate(request):
    date = request.POST.get("year")
    y=date.year
    print(y)
    current=y-date
    context={"age": current}
    return render(request,"age/display.html",context)


