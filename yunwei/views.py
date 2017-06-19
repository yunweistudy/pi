# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from yunwei.models import  user
from yunwei.regform import userform
def reguser(request):
    if request.method=='POST':
        getform=userform(request.POST)
        if getform.is_valid():
            getmodel=user()
            getmodel.user=getform.cleaned_data['user']
            getmodel.password=getform.cleaned_data['password']
            getmodel.tel=getform.cleaned_data['tel']
            getmodel.email=getform.cleaned_data['email']
            getmodel.group=getform.cleaned_data['group']
            getmodel.save()
            return  HttpResponse('注册用户成功')
        else:
            return HttpResponse('数据不合法')
    else:
        formini=userform()
        return render(request,'reg.html',locals())
def getpara(request):
    name=request.GET['name']
    nick=request.GET['nick']
    return HttpResponse(name+nick)

