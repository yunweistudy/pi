# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from datetime import datetime
# Create your models here.


class user(models.Model):
    # id = models.IntegerField(u'id',auto_created=True, primary_key=True, )
    user = models.CharField(u'用户名', max_length=20)
    password = models.CharField(u'密码', max_length=20, default='hello')
    group = models.CharField(u'组', max_length=20, null=False)
    tel = models.CharField(u'电话', max_length=20)
    email = models.EmailField(null='non')

class server(models.Model):
    # //要求唯一IP
    ip = models.CharField(u'IP地址', max_length=32,  unique=True)
    port = models.CharField(u'端口', max_length=5)
    username = models.CharField(u'用户名', max_length=20)
    password = models.CharField(u'密码', max_length=20)
    group = models.CharField(u'组', max_length=20)
    owner = models.CharField(u'拥有者', max_length=20)
    hostname = models.CharField(u'电脑名', max_length=20, default='localhost')

class history(models.Model):
    hostname = models.CharField(max_length=20)
    command = models.CharField(max_length=300)
    who = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)

class version(models.Model):
    project = models.CharField(max_length=20)
    version = models.CharField(max_length=20)
    #安装路径
    install_root = models.CharField(max_length=20)
    zipfile = models.FileField(upload_to='zipfile')
    note = models.TextField(max_length=50)
    uptime = models.DateTimeField(auto_now=True)
    up_user = models.CharField(max_length=20)

class xiangmu(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='项目名', )
    manager = models.CharField(max_length=30, verbose_name='项目经理')
    createtime = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    group = models.CharField(max_length=20, verbose_name='所属组')

class sqlserver(models.Model):
    type = models.CharField(max_length=20)
    port = models.IntegerField(range(1, 65535, 1))
    address = models.CharField(max_length=30, unique=True)
    createtime = models.DateTimeField(auto_now=True, )
    commit = models.TextField(max_length=30)
    user = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    db_user = models.CharField(max_length=20, default='root')
    db_password = models.CharField(max_length=20, default='hello')
    db_name = models.CharField(max_length=20, default='win')
    db_port = models.IntegerField(range(1, 999), default=22)

class sqlfile(models.Model):
    upuser = models.CharField(max_length=20)
    belong = models.CharField(max_length=20)
    commit = models.TextField()
    upfile = models.FileField(upload_to='sqlfiles')
    group = models.TextField(max_length=20)

class runsql(models.Model):
    runner = models.CharField(verbose_name=u'执行人', max_length=20)
    runserver = models.CharField(verbose_name=u'执行服务器', max_length=20)
    runtime = models.DateTimeField(verbose_name=u'执行时间', auto_now=True)
    runfile = models.CharField(verbose_name=u'执行文件', max_length=20)

class soft(models.Model):
    name = models.CharField(u'软件名称', max_length=20)
    install_time = models.DateTimeField(u'安装时间', auto_now=True)
    install_server = models.CharField(u'安装服务器', max_length=20)

class config(models.Model):
    path = models.CharField(u'配置路径', max_length=50)
    ver = models.CharField(u'版本号', max_length=10)
    softer = models.CharField(u'对应软件', max_length=20)
    uptime = models.DateTimeField(auto_now=True)
    commit = models.TextField(u'说明')
    conf_file = models.FileField(u'上传配置文件',  upload_to='config')

class git(models.Model):
    dage = (
        ("git@192.168.1.171:vod/vod-web.git", "git@192.168.1.171:vod/vod-web.git"),
        ("git@192.168.1.171:vod/customer.git", "git@192.168.1.171:vod/customer.git"),
        ("git@192.168.1.171:vod/customer-deploy.git", "git@192.168.1.171:vod/customer-deploy.git"),
    )
    gitserver = models.CharField(u'git服务器地址', max_length=100, choices=dage,default=dage[0])
    gitchoick = (
        ('qa', 'qa'),
        ('pre-build', 'pre-build'),
        ('online', 'online'),
        ('dev', 'dev'),
        ('master', 'master'),

    )
    gitbranch = models.CharField(u'git分支', max_length=20, choices=gitchoick, null=False, blank=False, default=gitchoick[0])
    choice = (
        ('pos', 'pos'), 
        ('ms', 'ms'), 
        ('customer', 'customer')
        # 前面是值 ，后面是显示
    )
    gitname = models.CharField(u'POS_OR_MS', max_length=50, choices=choice, default=choice[0])
    possqlphp = models.CharField(u'门店PHP执行脚本', max_length=150, default='null')
    mssqlphp = models.CharField(u'中央PHP执行脚本',  max_length=150,  default='null')
    notice = models.CharField(u'说明', max_length=50, default='请提前添加GIT免密码')
    deploy = models.CharField(u'是否部署', default='0', max_length=5)






