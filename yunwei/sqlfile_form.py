from django import forms
class sqlfile(forms.Form):
    upuser=forms.CharField(max_length=20)
    belong=forms.CharField(max_length=20)
    commit=forms.CharField(widget=forms.Textarea)
    upfile=forms.FileField()
    group=forms.CharField(max_length=20)