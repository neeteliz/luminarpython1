from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("<em>hello world</em>")
# def hello(request):
#     return HttpResponse("<em>welcome to django</em>")
def display(request):
    return render(request,"index.html")