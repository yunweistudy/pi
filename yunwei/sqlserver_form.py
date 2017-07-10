from django import forms
class sqlserver_form(forms.Form):
    type = forms.CharField(max_length=20)
    port = forms.IntegerField()
    address = forms.CharField(max_length=30,)
    commit = forms.CharField(widget=forms.Textarea)
    user = forms.CharField(max_length=20)
    group=forms.CharField(max_length=20,)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)