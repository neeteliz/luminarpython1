from django.shortcuts import render

# Create your views here.
def studentviewss(request):
    context={"names":["jaseentha","geetha","rahul","vinitha"]}
    return render(request,"student/studentview.html",context)