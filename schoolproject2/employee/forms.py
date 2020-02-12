from django import forms

class Employeedetail(forms.Form):
    ename=forms.CharField(max_length=100)
    eid=forms.CharField()
    esal=forms.CharField(max_length=250)
    design=forms.CharField(label="designation")