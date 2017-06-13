from django import forms
class AddForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'size': '30'}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    image=forms.FileField()
class ProfileForm(forms.Form):
    name=forms.CharField(max_length=50)
    picture=forms.ImageField()
class Myform(forms.Form):
    owner=forms.CharField(max_length=50)
    filename=forms.FileField()
class chunkform(forms.Form):
    store=forms.CharField(max_length=20,)
    addr=forms.CharField(max_length=20)
    sql=forms.FileField()


