from django import forms

class Formname(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    verify_email=forms.EmailField(label="enter ur email")
    text=forms.CharField(widget=forms.Textarea)