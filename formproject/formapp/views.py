from django.shortcuts import render
from .import forms
# Create your views here.

def formPage(request):
    form=forms.Formname()
    if request.method == 'POST':
        form = forms.Formname(request.POST)

    if form.is_valid():
        print("validation success")
        print("name: "+form.cleaned_data['name'])
        print("email: "+form.cleaned_data['email'])
        print("text: "+form.cleaned_data)
    return render(request,"formapp/forms.html",{'form':form})