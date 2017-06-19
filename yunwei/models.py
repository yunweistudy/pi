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
    def __unicode__(self):
        return self.user

class server(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    ip=models.CharField(max_length=32)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    allow_group=models.CharField(max_length=20)
    hostname=models.CharField(max_length=20,default='localhost')
class history(models.Model):
    hostname=models.CharField(max_length=20)
    command=models.CharField(max_length=300)
    who=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now=True)


