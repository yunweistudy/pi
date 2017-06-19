from django import forms
class userform(forms.Form):
    # id=forms.IntegerField()
    user=forms.CharField(max_length=20)
    group=forms.CharField(max_length=20)
    tel=forms.CharField(max_length=20)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    email=forms.EmailField()

class serverform(forms.Form):
    ip=forms.CharField(max_length=32)
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    hostname=forms.CharField(max_length=20)
