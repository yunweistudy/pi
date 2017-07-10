# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from  django import  forms
from yunwei.models import server
class server(forms.Form):
    ip=forms.CharField(max_length=50)
    username=forms.CharField(max_length=20)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    group=forms.CharField(max_length=32)
    owner=forms.CharField(max_length=20)
    port=forms.CharField(max_length=20)
    hostname=forms.CharField(max_length=32)
    # class Meta:
    #     module=server
    #     fields='__all__'

