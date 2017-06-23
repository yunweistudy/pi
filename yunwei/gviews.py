# -*- coding:utf-8 -*-
#批量执行命令
from fabric.api import *
from fabric.contrib import django
from django.http import HttpResponse
from fabric.contrib.console import confirm
from fabric.context_managers import *
django.project('myproject')
env.user='root'
env.passwords={
    'root@192.168.2.138:22':'world',
    'root@192.168.0.11:22':'123456'
}
# env.password='hello' 全部密码一样是这样设置
# env.hosts=["192.168.2.138"]
# env.host="192.168.2.138"
hosts=['192.168.2.138','192.168.0.11']
# env.host_string='192.168.2.236'
def locala(request):
    return HttpResponse('locala')
def remotea(request):
    list1=[]
    for i in hosts:
        env.host_string=i
        a=run('cat /root/a.txt')
        list1.append(a)
    return HttpResponse(list1)
#结束批量执行命令
#文件上传
localfile='/root/b.txt'
remotepath='/home/'
def putfile(request):
    for i in hosts:
        env.host_string = i
        result=put(localfile,remotepath)
    if result:
        return HttpResponse('good,上传成功')
    else:
        return HttpResponse('bad，上传失败')
