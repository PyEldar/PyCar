"""CarWebControl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from Main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name="admin"),
    #url(r'^$', views.Main, name="main"),
    url(r'^accelRotated/$', views.accelRotated, name="accelRotated"),
    url(r'^accel/$', views.accelRotated, name="accelRotated"),
    url(r'^getnumber/$', views.GetNumber, name="GetNumber"),
    url(r'^getpower/$', views.GetPower, name="GetPower"),
    url(r'^stopgo/$', views.StopGo, name="StopGo"),
    url(r'^$', views.accelRotated, name="accelRotated"),
]
