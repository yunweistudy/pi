#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .forms import   AddForm
from django.core.mail import send_mail
from .models import  User
from .models import Profile
import hashlib
import os
from .forms import  ProfileForm
def index(request):
    if request.method == 'POST':
        form= AddForm(request.POST,request.FILES)
        if form.is_valid():
            mydate=User()
            mydate.id=form.cleaned_data['id']
            mydate.name=form.cleaned_data['name']
            mydate.password=form.cleaned_data['password']
            mydate.image=form.cleaned_data['image']
            # salt='woda'+password
            # enp=hashlib.md5(salt.encode("utf8"))
            # realpassword=enp.hexdigest()
            tfile = request.FILES.get('image',None)
            realname=tfile.name
            size=tfile.size
            wanna=realname.split('.')
            tt=wanna[1]
            allow_types=['jpg','bmp','jif','zip',]
            if tt in allow_types and size <300000:
                mydate.save()
                res='good'
            else:
                res='bad'
            #return  HttpResponse(request.FILES)
            return render(request,'file.html',locals())
    else:
        form=AddForm()
    return render(request,'form.html',{'form':form})
def mail(request):
    content="""
    你好，唐先生
    这是一个测试梁山伯
    看一一下得不行和
    的
    """
    a=send_mail('hello  ,common on ',content,'tangzhonglang@juwang.cn',['157829939@qq.com'],fail_silently=False)
    return HttpResponse(a)
def log(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            u=User(id=id,name=name,password=password)
            p1=User.objects.get(name=name)
            password=p1.password
            return HttpResponse(password)
# def SaveProfile(request):
#     saved=0
#     tom='cat'
#     if request.method=="POST":
#         MyProfileForm=ProfileForm(request.POST,request.FILES)
#         if MyProfileForm.is_valid():
#             profile=Profile()
#             profile.name=MyProfileForm.cleaned_data['name']
#             profile.picture=MyProfileForm.cleaned_data['picture']
#             profile.save()
#             saved=1
#         else:
#             return HttpResponse('sorry')
#     return  render(request,'saved.html',locals())
def SaveProfile(request):
    saved=0
    tom='cat'
    if request.method=="POST":
        getfile=ProfileForm(request.POST,request.FILES)
        if getfile.is_valid():
            getmodel=Profile()
            getmodel.name=getfile.cleaned_data['name']
            getmodel.picture=getfile.cleaned_data['picture']
            getmodel.save()
            saved=1
        else:
            return HttpResponse('sorry')
    return  render(request,'saved.html',locals())
# def MyFile(request):
#     if request.method=="POST":
#         getform=myform(request.POST,request.FILES)
#         if getform.is_valid():
#             getform=mymode()
#             getform.owner=getform.cleaned_data['owner']
#             getform.filename=getform.cleaned_data['filename']
#             getform.save()
#             return HttpResponse('干得漂亮')
#         else:
#             mineform=myform()
#     return render(request,'file.html',locals())

def chunk(request):
    from blog.models import Chunk
    from blog.forms import chunkform
    # app=Chunk(id=1,store="浙江路店",addr='浙江路店地址')
    # app.save()
    # return  HttpResponse('看一下有没得数据')
    if request.method=="POST":
        getform=chunkform(request.POST,request.FILES)
        if getform.is_valid():
            getmodle=Chunk()
            getmodle.store=getform.cleaned_data['store']
            getmodle.addr=getform.cleaned_data['addr']
            getmodle.sql=getform.cleaned_data['sql']
            getmodle.save()
            return HttpResponse('干得漂亮')
    else:
        chunkform=chunkform()
        return render(request,'chunk.html',locals())



