from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from yunwei.models import version as version_model

def xuanzhe(request):
    if request.method=='POST':
        d=request.POST
        return HttpResponse(d)
    else:
        versions=version_model.objects.all().distinct()
        list=[]
        for i in versions:
            list.append(i.version)
        return render(request,'xuanzhe.html',locals())