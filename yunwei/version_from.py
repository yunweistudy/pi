from django import forms
class version(forms.Form):
    project=forms.CharField(max_length=20)
    version =forms.CharField(max_length=20)
    install_root=forms.CharField(min_length=5)
    zipfile=forms.FileField()
    note=forms.CharField(widget=forms.Textarea)
