from django import forms

class Addproject(forms.Form):
    Title = forms.CharField(max_length=100, required=True, label='project title')
