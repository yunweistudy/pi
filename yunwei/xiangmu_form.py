from django import forms
class xiangmu(forms.Form):
    name=forms.CharField(max_length=20,)
    manager=forms.CharField(max_length=20)
    group=forms.CharField(max_length=20)