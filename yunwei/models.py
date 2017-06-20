# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    # id=models.IntegerField(u'id',auto_created=True,primary_key=True,)
    user=models.CharField(u'用户名',max_length=20,)
    password=models.CharField(u'密码',max_length=20,default='hello')
    group=models.CharField(u'组',max_length=20,null=False)
    tel=models.CharField(u'电话',max_length=20)
    email=models.EmailField(null='non')

class server(models.Model):
    ip=models.CharField(max_length=32)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    own_group=models.CharField(max_length=20)
    hostname=models.CharField(max_length=20,default='localhost')
class history(models.Model):
    hostname=models.CharField(max_length=20)
    command=models.CharField(max_length=300)
    who=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now=True)
class version(models.Model):
    project=models.CharField(max_length=20)
    version=models.CharField(max_length=20)
    #安装路径
    install_root=models.CharField(max_length=20)
    zipfile=models.FileField(upload_to='zipfile')




