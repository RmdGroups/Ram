"""Ram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("index/",views.index),
    path("gallery/",views.gallery),
    path("send/",views.send),
    path("bar/",views.bar),
    path("search1/",views.search1),
    path("search2/",views.search2),
    path("about/",views.about),
    path("show/",views.show),
    path("edit<int:idno>/",views.edit),
    path("update<int:idno>/",views.update),
    path("delete<int:idno>/",views.delete),

]
