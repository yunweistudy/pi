# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from yunwei.models import  user
from yunwei.models import  version as mversion
from yunwei.regform import userform
from yunwei.version_from import version as versionform
from yunwei.models import server as servermodel
from yunwei.server_form import  server as serverfom
from django.http import HttpResponseRedirect
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime

def reguser(request):
    if request.method=='POST':
        getform=userform(request.POST)
        if getform.is_valid():
            # getmodel=user()
            # getmodel.user=getform.cleaned_data['user']
            # getmodel.password=getform.cleaned_data['password']
            # getmodel.tel=getform.cleaned_data['tel']
            # getmodel.email=getform.cleaned_data['email']
            # getmodel.group='null'
            moment=getform.save()
            moment.save()
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
def showuser(request):
    show=user.objects.all()
    return render(request,'showuser.html',locals())
# Person.objects.all()[:10] 切片操作，获取10个人，不支持负索引，切片可以节约内存
def deluser(request):
    deluser=user.objects.filter(id=1)
    deluser.delete()
    return HttpResponse('good')
def upuser(request):
    upuser=user.objects.filter(id=2)
    upuser.update(id=1)
    # models.UserInfo.objects.filter(user='yangmv').update(pwd='520')
    # 或者
    # obj = models.UserInfo.objects.get(user='yangmv')
    # obj.pwd = '520'
    # obj.save()
    return  HttpResponse('upgood')


def index(request):
    user=request.COOKIES.get('username')
    if user:
        return render(request,'index.html',locals())
    else:
        return HttpResponseRedirect('/login/')
def login(request):
    if request.method=='POST':
        passwrod1=request.POST['password']
        user1=request.POST['user']
        show=user.objects.filter(id=1)
        # return render(request,'showuser.html',locals())
        if user.objects.filter(user=user1,password=passwrod1):
            response = HttpResponseRedirect('/index/')
            response.set_cookie('username', user1, 3600)
            return response
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request,'login.html',locals())







