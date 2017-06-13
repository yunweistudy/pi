
#coding=utf-8

from django.db import models
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    def __str__(self):
        return self.title
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.FileField(upload_to='picture')
    def __unicode__(self):
        return self.name
class Profile(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='picture')
    class Meta:
        db_table="profile"
class MyFile(models.Model):
    owner=models.CharField(max_length=50)
    filename=models.FileField(upload_to='myfile')
class Chunk(models.Model):
    id=models.IntegerField(primary_key=True)
    store=models.CharField(max_length=20)
    addr=models.CharField(max_length=20)
    sql=models.FileField(upload_to='mysql')



