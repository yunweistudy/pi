from django.forms import ModelForm
from django import forms
from yunwei.models import config  as configmodel
class configform(ModelForm):
    # name=forms.CharField(max_length=20)
    class Meta:
        model=configmodel
        fields='__all__'
    # path=forms.CharField(max_length=20)
    # server=forms.CharField(max_length=20)
    # conf_file=forms.FileField()
    # commit=forms.CharField(widget=forms.Textarea)

