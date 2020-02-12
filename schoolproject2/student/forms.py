from django import forms

class Studentname(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    crse=forms.CharField(max_length=250)