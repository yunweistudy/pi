#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Company
from myapp.models import User
import difflib
import psutil
import subprocess
# Create your views here.
def add(request):
    c=Company(full_name='集团',address='大重庆洗脚城',tel=88888)
    try:
        c.save()
        return HttpResponse('good')

    except:
        return HttpResponse('bad')
def adduser(request):
        u=User(name='欢欢')
        u.save()
        return HttpResponse('bye,看一下有没得数据')
def getcom(request):
    c=Company.objects.all().order_by('-id').distinct()
    return render(request,'getcom.html',{'coms':c})
def mem(request):
    c=psutil.virtual_memory()
    return  render(request,'mem.html',{'mem':c})
def disk(request):
    a=psutil.disk_partitions()
    return  HttpResponse(a)
def io(request):
    i=psutil.disk_io_counters(perdisk=True)
    return HttpResponse(i)
def time(request):
    t=psutil.boot_time()
    t1=t/60/60/24/60
    return HttpResponse(t1)
def pid(request):
    p=psutil.pids()
    names=[]
    for i in p:
        o=psutil.Process(i)
        name=o.name()
        names.append([name])
    return render(request,'pid.html',locals())
def dif(requtest):
    s1="""
    hello 
    world
    a
    """
    s2="""
    hello
    kitty
    b
    """
    d=difflib.Differ()
    ddd=d.compare(s1.splitlines(),s2.splitlines(),)
    return  HttpResponse(ddd)
def command(request):
    output=subprocess.call(["ls","-l"],shell=True)
    show=subprocess.check_output(["ls","-l"],shell=True)
    return  HttpResponse(show)
def mmail(request):
    #这里是独立邮件测试
    import smtplib
    import string
    HOST="smtp.exmail.qq.com"
    SUBJECT="这里是测试主题"
    TO="157829939@qq.com"
    FROM="tangzhonglang@juwang.cn"
    text="这里是邮件内容，噢噢"
    server=smtplib.SMTP()
    server.connect(HOST,"25")
    server.login("tangzhonglang@juwang.cn","Fuck9939")
    server.sendmail(FROM,[TO],"454545454545")
    server.quit()
    return  HttpResponse("alal")
def ppe(request):
    import pexpect
    child = pexpect.spawn('ssh root@192.168.2.236')
    index = child.expect(['Are.*', 'password:'])
    if (index == 0):
        child.sendline("yes")
        child.expect("password:")
        child.sendline("hello")
    else:
        child.sendline("hello")
    child.expect('#')
    child.sendline('cd /home && touch fucking.txt')
    child.expect('#')
    child.sendline('yum install -y httpd')
    cmd='scp /data/god root@192.168.2.236:/home/'
    child2=pexpect.spawn(cmd)
    child2.expect('.*password.*')
    child2.sendline('hello')
   # child3=pexpect.spawn('yum install -y httpd')这是错误示范，命令是在本地执行的 OH FUCK!
   # child3.expect('#')
    cmd2='yum install -y httpd'
    child3=pexpect.spawn('ssh root@192.168.2.236 ',[cmd2] )
    child3.sendline("hello")
    return HttpResponse(cmd2+cmd2)
def getter(request):
        if request.method=='GET':
            a='one'
            name=request.GET.get('name')
        else:
            a='two'
        return  HttpResponse(a+name)





