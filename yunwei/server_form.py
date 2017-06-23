from  django import  forms
class server(forms.Form):
    ip=forms.CharField(max_length=32)
    username=forms.CharField(max_length=20)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    own_group=forms.CharField(max_length=32)
    hostname=forms.CharField(max_length=32)
