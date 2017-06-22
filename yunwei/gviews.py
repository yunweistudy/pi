# -*- coding:utf-8 -*-
# from django.http import HttpResponse
# from django.shortcuts import render
# from fabric.api import *
# from fabric.contrib import django
# from fabric.contrib.console import confirm
# env.user='root'
# env.password='hello'
# env.hosts=['192.168.2.138']
# #执行本地命令
# def locala(request):
#     local('touch /root/b1.txt ')
#     local('touch /root/b2.txt ')
#     a='good'
#     return HttpResponse(a)
# #执行远程命令
# @hosts('root@192.168.2.138')
# def remotea(request):
#     run('mkdir -p /home/wodada')
#     run('mkdir -p /home/wodada1')
#     run('mkdir -p /home/wodada2')
#     return HttpResponse("pang")

from fabric.api import *
from fabric.contrib import django
from django.http import HttpResponse
django.project('myproject')
env.user='root'
env.password='hello'
# env.hosts=["192.168.2.138"]
# env.host="192.168.2.138"
hosts=['192.168.2.236','192.168.2.138']
# env.host_string='192.168.2.236'
def locala(request):
    return HttpResponse('locala')
def remotea(request):
    print("env:", env.hosts, env.host, env.host_string)
    # run('mkdir -p /data/go/go/do2')
    for i in hosts:
        env.host_string=i
        run('mkdir -p /data/come1')
    return HttpResponse('hello')
