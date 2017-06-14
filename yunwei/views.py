# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from yunwei.models import  user
from yunwei.regform import userform
def reguser(request):
    if request.method=='POST':
        getform=userform(request.POST)
        if getform.is_valid():
            getmodel=user()
            getmodel.id=getform.cleaned_data['id']
            getmodel.user=getform.cleaned_data['user']
            getmodel.password=getform.cleaned_data['password']
            getmodel.tel=getform.cleaned_data['tel']
            getmodel.save()
            return  HttpResponse('注册用户成功')
    else:
        formini=userform()
        return render(request,'reg.html',locals())

