# -*- coding:utf-8 -*-
#批量执行命令
import  time
import  os
from fabric.api import *
from yunwei.models import server as servermodel
from yunwei.server_form import  server as serverfom
from django.http import HttpResponseRedirect
from django.template import Context
from fabric.context_managers import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from yunwei.version_from import version as version_form
from yunwei.models import version as version_model
from  yunwei.models import server
from yunwei.models import xiangmu as xiangmu_model
from yunwei.models import sqlserver  as sqlserver_model
from yunwei.sqlserver_form import sqlserver_form
from yunwei.xiangmu_form import xiangmu as xiangmu_form
from yunwei.sqlfile_form import sqlfile as sqlfile_form
from yunwei.models import sqlfile as sqlfile_model
from yunwei.models import runsql  as runsql_model
from yunwei.formes import runsql as runsql_form
from yunwei.models import soft as soft_model
from yunwei.soft_form import softform as soft_form
from yunwei.models import config as config_model
from yunwei.config_form import configform as config_form
from  yunwei.models import git as git_model
from  yunwei.git_form import git_form
# django.project('myproject')
# env.user='root'
# env.passwords={
#     'root@192.168.2.138:22':'world',
#     'root@192.168.0.11:22':'123456'
# }
# env.password='hello' 全部密码一样是这样设置
# env.hosts=["192.168.2.138"]
# env.host="192.168.2.138"
# hosts=['192.168.2.138','192.168.0.11']
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
#测试从数据库得到IP地址和密码
# def sujuku(request):
#     from yunwei.models import server
#     from django.shortcuts import render
#     info=server.objects.filter(owner='tang')
#     lister=[]
#     for i in info:
#         env.user=i.username
#         env.password = i.password
#         env.host_string = i.ip
#         env.port=i.port
#         # result=put(localfile,remotepath)
#         result=run('systemctl start httpd')
#         lister.append(result)
#     return render(request,'sujuku.html',locals())
#版本管理
def version(request):
    if request.method=='POST':
        getform=version_form(request.POST,request.FILES)
        if getform.is_valid():
            getmodel=version_model()
            getmodel.project=getform.cleaned_data['project']
            getmodel.version=getform.cleaned_data['version']
            getmodel.install_root=getform.cleaned_data['install_root']
            getmodel.zipfile=getform.cleaned_data['zipfile']
            getmodel.note=getform.cleaned_data['note']
            getmodel.up_user='daodao'
            getfile=request.FILES.get('zipfile',None)
            file_name=getfile.name
            file_size=getfile.size
            allow_type=['zip','xls','rar']
            real_name=file_name.split('.')
            if real_name[1] in allow_type:
                getmodel.save()
                return HttpResponse('good')
            else:
                return HttpResponse('上传非法文件，运维的同学来打你来了')
        else:
            return HttpResponse('数据验证失败！！')
    else:
        #得到参数
        para=request.GET['para']
        #得到表对象
        ini_form=version_form()
        ini_verson=version_model.objects.all()
        if para=='look':
            return render(request,'lookversion.html',locals())
        elif para=='add':
            #得到项目
            project=xiangmu_model.objects.all().distinct()
            projects=[]
            for i in project:
                projects.append(i.name)
            return render(request,'version.html',locals())
#部署管理
def deploey(request):
    if request.method=='POST':
        #获取开始处理的服务器
        doservers=request.POST.getlist('boxes',[])
        #获取开始处理的项目
        doprojects=request.POST.get('projects')
        #获取开始处理的版本
        doversions=request.POST.get('versions')
        lister=[]
        for i in doservers:
            #获取每一个服务器的信息
            info=server.objects.all().filter(ip=i).filter(group='wuhuan')
            # 获取本地文件路径
            lofilea = version_model.objects.all().filter(project=doprojects).get(version=doversions)
            lofileb=lofilea.zipfile.name
            lofile_pre='/data/python/media/'
            #最终上传文件
            lofile=lofile_pre+lofileb
            #最终上传目的目录
            uppath='/data/wwwsrc/'
            for l in info:
                env.user=l.username
                env.port=l.port
                env.host_string=l.ip
                env.password=l.password
                #免密码的话不用任何配置，只需要按正常免密码配置到authorized_keys,600就可以了,上面的不影响
            #测试命令成功
            # result=run('cat /root/a.txt')
            #开始上传文件
            put_result=put(lofile,uppath)
            #解压文件
            run('mkdir -p  /data/wwwsrc')
            with cd('/data/wwwsrc'):
                #拼解压命令
                zipfile=lofileb.split('/')
                zipfilk=zipfile[1]
                zipfilm=zipfilk.split('.')
                zipall='unzip -o   -d  '+zipfilm[0]+'  '+zipfilk
                run(zipall)
            #先建个目录在说
            run('mkdir -p  /data/wwwroot',)
            #切换目录后操作
            with cd('/data/wwwroot'):
                run('rm -f vodpos')
                #拼接软链地址
                a1='/data/wwwsrc/'
                a2=a1+zipfilm[0]
                link= 'ln -s  '+a2+'  vodpos'
                run(link)
        return HttpResponse('处理完成！')
    else:
        #获取服务器
        getserver=server.objects.all()
        #得到项目名
        getproject=xiangmu_model.objects.all().distinct()
        #获取版本
        getversion=version_model.objects.values('version').distinct()
        return render(request,'deploy.html',locals())
#日志读取测试
def log(request):
    if request.method=='POST':
        pass
    else:
        f='/var/log/dmesg'
        f_object=open(f,)
        gans=[]
        #换行读取 GOOD!
        for gan in f_object:
            print gan
            gans.append(gan)
        #readline不会给到变量
        gg=f_object.readline()
        return render(request,'log.html',locals())
#数据库管理
def sqlser(request):
    if request.method=='POST':
        get_sqlserver_form=sqlserver_form(request.POST)
        if get_sqlserver_form.is_valid():
            get_sqlserver_model=sqlserver_model()
            get_sqlserver_model.type=get_sqlserver_form.cleaned_data['type']
            get_sqlserver_model.port=get_sqlserver_form.cleaned_data['port']
            get_sqlserver_model.address=get_sqlserver_form.cleaned_data['address']
            get_sqlserver_model.commit=get_sqlserver_form.cleaned_data['commit']
            get_sqlserver_model.user=get_sqlserver_form.cleaned_data['user']
            get_sqlserver_model.password=get_sqlserver_form.cleaned_data['password']
            get_sqlserver_model.save()
            return  HttpResponse('保存数据库成功')
        else:
            return HttpResponse('数据可能有问题')

    else:
        para=request.GET['para']
        if para=='look':
            ini_sqlserver_model=sqlserver_model.objects.all()
            return  render(request,'looksqlserver.html',locals())
        elif para=='add':
            ini_sqlserver_form=sqlserver_form()
            return render(request,'add_sqlserver.html',locals())
#处理SQL文件上传
def dosqlfile(request):
    if request.method=='POST':
        get_sqlfile_form=sqlfile_form(request.POST,request.FILES)
        if get_sqlfile_form.is_valid():
            get_sqlfile_model=sqlfile_model()
            get_sqlfile_model.upuser=get_sqlfile_form.cleaned_data['upuser']
            get_sqlfile_model.belong=get_sqlfile_form.cleaned_data['belong']
            get_sqlfile_model.commit=get_sqlfile_form.cleaned_data['commit']
            get_sqlfile_model.upfile=get_sqlfile_form.cleaned_data['upfile']
            get_sqlfile_model.group=get_sqlfile_form.cleaned_data['group']
            #得到文件名
            get_file_=request.FILES.get('upfile',None)
            get_file_name=get_file_.name
            fenli=get_file_name.split('.')
            allow_ty=['sql']
            if fenli[1] in allow_ty:
                get_sqlfile_model.save()
                return HttpResponse('上传SQL文件成功')
            else:
                return HttpResponse('上传非法文件,运维的同学来打你来了')
        else:
            return HttpResponse('数据无效')
    else:
        ini_sqlfile_form=sqlfile_form()
        return render(request,'sqlfile.html',locals())

def linuxserver(request):
    if request.method=='POST':
        postform=serverfom(request.POST)
        if postform.is_valid():
            getmodel=servermodel()
            getmodel.ip=postform.cleaned_data['ip']
            getmodel.username=postform.cleaned_data['username']
            getmodel.password=postform.cleaned_data['password']
            getmodel.hostname=postform.cleaned_data['hostname']
            getmodel.group=postform.cleaned_data['group']
            getmodel.port=postform.cleaned_data['port']
            getmodel.owner=postform.cleaned_data['owner']
            getmodel.save()
            # return HttpResponseRedirect(reversed("yunwei.views.server"))
            return HttpResponse('good,添加服务器成功')
        else:
            return HttpResponse('bad,数据不合法')
    else:
        #获取GET参数
        para=request.GET['para']
        myserver = servermodel.objects.filter(group='wuhuan')
        getform = serverfom()
        if para=='look':
            return render(request,'lookserver.html',locals())
        elif para=='add':
            return render(request,'server.html',locals())
#项目管理
def xiangmuf(request):
    if request.method=='POST':
        get_xiangmu_form=xiangmu_form(request.POST)
        if get_xiangmu_form.is_valid():
            get_xiangmu_model=xiangmu_model()
            get_xiangmu_model.name=get_xiangmu_form.cleaned_data['name']
            get_xiangmu_model.manager=get_xiangmu_form.cleaned_data['manager']
            get_xiangmu_model.group=get_xiangmu_form.cleaned_data['group']
            get_xiangmu_model.save()
            return HttpResponse('good')
        else:
            return HttpResponse('数据不合法')
    else:
        para=request.GET['para']
        myxiangmu=xiangmu_model.objects.filter(group='wuhuan')
        if para=='look':
            return  render(request,'lookproject.html',locals())
        elif para=='add':
            ini_xiangmu_form=xiangmu_form(request.POST)
            return render(request,'addproject.html',locals())
def runsql(request):
    if request.method=='POST':
        #得到需要执行的服务器列表
        get_servers=request.POST.getlist('linuxserver',[])
        #得到需要执行的数据文件
        get_sqlfile=request.POST.get('sqlfile')
        realfile='/data/python/media/'+get_sqlfile
        #开始执行
        for i in get_servers:
            #得到服务器相关信息
            sqlservers=sqlserver_model.objects.get(address=i)
            #得到用服务器户名密码
            getuser=sqlservers.user
            getpassword=sqlservers.password
            getport=sqlservers.port
            #得到数据库用户密码
            getdb_user=sqlservers.db_user
            getdb_password=sqlservers.db_password
            getdb_port=sqlservers.db_port
            getdb_name=sqlservers.db_name
            #得到数据库各类
            getdbtype=sqlservers.type
            if getdbtype=='mysql':
                env.user=getuser
                env.port=getport
                env.password=getpassword
                env.host_string=i
                #组装SQL
                sqls='mysql -u'+getdb_user+' -p'+getdb_password+' -P'+str(getdb_port)+'   \t'+getdb_name+ '  <  '+ realfile+'   >>/data/sql/runsql.txt'
                run(sqls)
                return HttpResponse('执行成功')
            elif getdbtype=='postgres':
                return HttpResponse('this is postgres')
            else:
                return HttpResponse('暂不支持的数据库')
        return HttpResponse('')
    else:
        #得到RUNSQL表单
        ini_runsql_form=runsql_form()
        #得到数据库服务器列表
        ini_linuxser=sqlserver_model.objects.filter(group='wuhuan')
        #得到SQL文件列表
        ini_sqlfile=sqlfile_model.objects.filter(group='wuhuan')
        return render(request,'runsql.html',locals())
#软件安装
def soft(request):
    if request.method=='POST':
        get_soft_name=request.POST['softname']
        get_soft_servers=request.POST.getlist('servers',[])
        #开始安装
        for ss in get_soft_servers:
            #拼接YUM
            word='yum install -y '+get_soft_name
            #获取服务器对象
            getserver=server.objects.get(ip=ss)
            env.host_string=getserver.ip
            env.port=getserver.port
            env.password=getserver.password
            run(word)
        return HttpResponse(word)
    else:
        #获取服务器列表
        ini_ser=server.objects.all()
        #获取初始表单
        ini_soft_form=soft_form()
        para=request.GET['para']
        if para=='install':
            return  render(request,'addsoft.html',locals())
        elif para=='look':
            return render(request,'looksoft.html')

#配置管理
def configer(request):
    if request.method=='POST':
        get_configform=config_form(request.POST,request.FILES)
        if get_configform.is_valid():
            #初始一个配置文件MODEL
            get_configmodel=config_model()
            #先存POST过来的数据到数据库
            get_configform.save().save()
            return HttpResponse('good')
        else:
            return HttpResponse('可能数据有问题')
    else:
        para=request.GET['para']
        if para=='add':
            #得到配置文件表格
            ini_config_form=config_form()
            #得到服务器列表
            conf_server=server.objects.all()
            return  render(request,'add_config.html',locals())
        elif para=='look':
            return HttpResponse('还在开发中')
        else:
            return HttpResponse('参数不对')
#执行配置添加
def toconfig(request):
    if request.method=='POST':
        get_server=request.POST.getlist('server',[])
        get_soft=request.POST['soft']
        get_ver=request.POST['ver']
        #拼接原始文件
        a1='/data/python/media/'
        b1=config_model.objects.filter(ver=get_ver).filter(softer=get_soft)
        for kk in b1:
            #得到真实文件
            a2=kk.conf_file.name
            a3=a2.split('/')
            a4=a3[1]
            #a4是纯文件名
            mv='mv   '+a4+'   '+a4+'.bak'
            # 目的目录
            b2=kk.path
        realpath=a1+a2
        #遍历执行
        for  i  in get_server:
            #得到服务器信息
            goserver=server.objects.get(ip=i)
            env.user=goserver.username
            env.password=goserver.password
            env.port=goserver.port
            env.host_string=i
            #备份源文件,如果没有会出错
            with cd(b2):
                run(mv)
            #开始上传
            put(realpath,b2)
            return HttpResponse('上传成功')
    else:
        #初始表单
        ini_configform=config_model.objects.all()
        #初始服务器,临时定义一个过滤组，按需求改
        ini_server=server.objects.filter(group='wuhuan')
        return render(request,'toconfig.html',locals())

def git(request):
    if request.method=='POST':
        if request.POST['action']=='add':
            get_gitform=git_form(request.POST)
            if get_gitform.is_valid():
                get_gitmodel=git_model()
                get_gitmodel.gitserver=get_gitform.cleaned_data['gitserver']
                get_gitmodel.gitbranch=get_gitform.cleaned_data['gitbranch']
                sdate=time.strftime('%Y-%m-%d-%H%M',time.localtime(time.time()))
                savegitname=get_gitform.cleaned_data['gitname']+sdate
                get_gitmodel.gitname=savegitname
                get_gitmodel.notice=get_gitform.cleaned_data['notice']
                get_gitmodel.possqlphp=get_gitform.cleaned_data['possqlphp']
                get_gitmodel.mssqlphp = get_gitform.cleaned_data['mssqlphp']
                get_gitmodel.save()
                return HttpResponse('添加版本成功！')
            else:
                return HttpResponse('添加版本失败')
        elif request.POST['action']=='deploy':
            getserver=request.POST.getlist('servers',[])
            getgitserver=request.POST['gitserver']
            getbranch=request.POST['branch']
            getposphp=request.POST['possqlphp']
            getmsphp=request.POST['mssqlphp']
            getversion=request.POST['version']
            getversion2=getversion.strip(" ")
            # result=git_model.objects.get(gitname=getversion2)
            # return HttpResponse(result.gitname)
            if 'pos' in getversion:
                os.system('cd /data/git/vod-web  && git checkout   '+getbranch+' &&  git pull '+'  && rm -fr /data/git/vod-web/ms')
                #打包
                wor='tar -zcvf' +getversion+'.tar  '+'  *'
                os.system('cd /data/git/vod-web  && '+wor )
                os.system('cd  /data/git/vod-web && mv -f '+getversion+'.tar'+'  '+'/data/git/')
                #上传
                for xx in getserver:
                    real=server.objects.get(ip=xx)
                    env.host_string=real.ip
                    env.port=real.port
                    env.user=real.username
                    env.password=real.password
                    thisfile='/data/git/'+getversion+'.tar'
                    thisfile2=thisfile.replace(' ','')
                    #远程目录，这个看要不要接收处理，先写死吧
                    re_path='/data/src'
                    put(thisfile2,re_path)
                    #解压
                    with cd('/data/src'):
                        runword='tar -zxvf '+getversion+'.tar'+'  -C '+getversion
                        run('rm -fr  '+getversion+'  &&'+'mkdir  '+getversion)
                        run(runword)
                    with cd('/data/wwwroot'):
                        run('rm -f /data/wwwroot/vodpos')
                        linkru='ln     -s     /data/src/x'+getversion+'   vodpos '
                        links=linkru.replace('x ','')
                        olink='/data/src/x'+getversion
                        ooklink=olink.replace('x ','')
                        run(links)
                    with cd(ooklink):
                        if getposphp=='null':
                            pass
                        else:
                            run('/usr/local/php/7.0.8/bin/php   '+getposphp)
                    run('chown -R www.www /data/src')
                    run('chown -R www.www  /data/wwwroot/vodpos')
                return HttpResponse('POS处理完毕')
            elif 'ms' in getversion:
                os.system('cd /data/git/vodms  && git checkout   '+getbranch+'&& git pull ')
                # 打包
                wor = 'tar -zcvf' + getversion + '.tar  ' + '  *'
                os.system('cd /data/git/vodms  && ' + wor)
                os.system('cd  /data/git/vodms && mv -f ' + getversion + '.tar' + '  ' + '/data/git/')
                for msq in getserver:
                    realms=server.objects.get(ip=msq)
                    env.host_string=realms.ip
                    env.port=realms.port
                    env.user=realms.username
                    env.password=realms.password
                    localmsfile='/data/git/x'+getversion+'.tar'
                    localmsfile2=localmsfile.replace('x ','')
                    remote_ms_path='/data/src'
                    #上传
                    put(localmsfile2,remote_ms_path)
                    #解压
                    with cd('/data/src'):
                        #准备目录
                        getdir='rm -fr /data/srcx'+getversion+'  &&  mkdir -p /data/src/x'+getversion
                        getdir2=getdir.replace('x ','')
                        run(getdir2)
                        tarword='tar -zxvf '+getversion+'.tar'+'  -C'+getversion
                        run(tarword)
                        #更连接
                    with cd('/data/wwwroot'):
                        run('rm -fr /data/wwwroot/vodms')
                        linkru = 'ln     -s     /data/src/x' + getversion + '   vodms '
                        links = linkru.replace('x ', '')
                        olink = '/data/src/x' + getversion
                        ooklink = olink.replace('x ', '')
                        run(links)
                    with cd(ooklink):
                        if getposphp == 'null' and getmsphp=='null':
                            pass
                        elif getposphp!='null' and getmsphp=='null':
                            run('/usr/local/php/7.0.8/bin/php   ' + getposphp)
                        elif getposphp=='null'  and getmsphp!='null':
                            run('/usr/local/php/7.0.8/bin/php ' + getmsphp)
                        elif getposphp!='null' and getmsphp!='null':
                            run('/usr/local/php/7.0.8/bin/php ' +getposphp)
                            run('/usr/local/php/7.0.8/bin/php '+getmsphp)
                    # 改一下权限
                    run('chown -R www.www /data/src/')
                    run('chown -R www.www  /data/wwwroot/vodms')
                return HttpResponse('MS处理完成')
            elif 'customer' in getversion :
                #git@192.168.1.171:vod/customer-deploy.git对应 是预上线 qa分支，线上master分支
                #git@192.168.1.171:vod/customer.git 这个对应 QA服务上的qa分支
                os.system('cd /data/git/customer  && git checkout   ' + getbranch + '&& git pull ')
                # 打包
                wor = 'tar -zcvf' + getversion + '.tar  ' + '  *'
                os.system('cd /data/git/customer  && ' + wor)
                os.system('cd  /data/git/customer && mv -f ' + getversion + '.tar' + '  ' + '/data/git/')
                #上传
                for xx in getserver:
                    real=server.objects.get(ip=xx)
                    env.host_string=real.ip
                    env.port=real.port
                    env.user=real.username
                    env.password=real.password
                    thisfile='/data/git/'+getversion+'.tar'
                    thisfile2=thisfile.replace(' ','')
                    #远程目录，这个看要不要接收处理，先写死吧
                    re_path='/data/src'
                    put(thisfile2,re_path)
                    #解压
                    with cd('/data/src'):
                        runword='tar -zxvf '+getversion+'.tar'+'  -C '+getversion
                        run('rm -fr  '+getversion+'  &&'+'mkdir  '+getversion)
                        run(runword)
                    with cd('/data/wwwroot'):
                        run('rm -f  /data/wwwroot/customer')
                        linkru='ln     -s     /data/src/x'+getversion+'   customer '
                        links=linkru.replace('x ','')
                        olink='/data/src/x'+getversion
                        ooklink=olink.replace('x ','')
                        run(links)
                    with cd('/data/wwwroot/customer'):
                        run('cp -rf /home/www/custom/customer/vendor/ ./')
                        run('cp -rf /home/www/custom/customer/.env ./')
                    run('chown -R www.www /data/src/')
                    run('chown -R www.www  /data/wwwroot/customer')
                return HttpResponse('customer处理完成！')
            else:
                return HttpResponse('not ms,pos,customer')
        else:
            return HttpResponse('我顶你个肺')
    else:
        para=request.GET['para']
        if para=='look':
            pass
        elif para=='add':
            # return HttpResponse('开始添加git版本')
            ini_git_form=git_form()
            return  render(request,'git.html',locals())
        elif para=='deploy':
            ini_git_model=git_model.objects.all().distinct()
            #得到GIT服器唯一值
            gitser=git_model.objects.values('gitserver').distinct()
            #得到倒序的5个版本值
            getver=git_model.objects.values('gitname').order_by('id').reverse()[:5]
            #得到分支
            inibranch=git_model.objects.values('gitbranch').distinct()
            #门店PHPSQL
            iniposphp=git_model.objects.values('possqlphp').distinct()
            #中央PHPSQL
            inimsphp=git_model.objects.values('mssqlphp').distinct()
            ini_server_modle=server.objects.filter(group='wuhuan')
            return  render(request,'gitdeploy.html',locals())




