"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp import  views
from blog import views as bviews
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', views.add,name='add'),
    url(r'^adduser',views.adduser,name='adduser'),
    url(r'^getcom/',views.getcom,name='getcom'),
    url(r'^form/',bviews.index,name='form'),
    url(r'^mail/',bviews.mail,name='mail'),
    url(r'^log/',bviews.log,name='log'),
    url(r'^profile/',TemplateView.as_view(template_name = 'profile.html'),name='profile'),
    url(r'^save/',bviews.SaveProfile,name='save'),
    # url(r'^myfile',bviews.MyFile,name='myfile')
    url(r'^mem/',views.mem,name='mem'),
    url(r'mmail/',views.mmail,name='mmail'),
    url(r'^ppe/',views.ppe,name='ppe'),
    url(r'^getter',views.getter,name='getter'),
    url(r'^index/',bviews.index,name='index'),
    url(r'^chunk/',bviews.chunk,name='chunk')
]
