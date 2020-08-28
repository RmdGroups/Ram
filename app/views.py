from django.shortcuts import render
from.models import Reg
import random
import math
import re
import qrcode


import numpy as np
import matplotlib.pyplot as plt

from datetime import date

def home(request):
    return render(request,"Home1.html")

def index(request):
    return render(request,"index.html")
#   dgt = "0123456789"
 #   otp = ""
  #  for i in range(4):
   #     otp += dgt[math.floor(random.random() * 10)]
    #fname=request.POST.get("fname")
    #lname=request.POST.get("lname")
    #phone=request.POST.get("phone")
    #gender=request.POST.get("gender")
    #Register(idno=otp,fname=fname,lname=lname,phone=phone,gender=gender).save()
    #return render(request,"Home.html")


def send(request):
    dgt = "0123456789"
    otp = ""
    for i in range(2):
        otp += dgt[math.floor(random.random() * 10)]
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    da=request.POST.get("date")

    gender=request.POST.get("gender")
    blood=request.POST.get("blood")
    village=request.POST.get("village")
    mandal=request.POST.get("mandal")
    district=request.POST.get("district")

    phone = request.POST.get("phone")
    a=re.fullmatch("[6-9]\d{9}",phone)

    today=date.today()
    ab = da[8:10]
    bc = da[5:7]
    ca = da[0:4]
    age = int(today.year) - int(ca) - ((int(today.month), (int(today.day))) < (int(bc), int(ab)))
    age_Rmd=age>18
    if a!=None:
        Reg(idno=otp,fname=fname,lname=lname,date=da,gender=gender,blood=blood,village=village,mandal=mandal,district=district,phone=phone).save()
        qr=Reg.objects.filter()
        list=[]
        for i in qr:
            abc=i.blood
            list.append(abc)
            Ap=list.count("A+")
            An=list.count("A-")
            Bp=list.count("B+")
            Bn=list.count("B-")
            ABp=list.count("AB+")
            ABn=list.count("AB-")
            Op=list.count("O+")
            On=list.count("O-")
            objects = ('A+','A-','B+','B-', 'AB+', 'AB-', 'O+', 'O-')
            y_pos = np.arange(len(objects))
            performance = [Ap,An,Bp,Bn,ABp,ABn,Op,On]
            plt.bar(y_pos, performance, align='center', alpha=1)
            plt.xticks(y_pos, objects)
            plt.ylabel('Blood donor')
            plt.title('Rmd Blood Group Websites')
            plt.savefig(r"app/static/images/Bar.png")
            plt.show()
        name= lname+"   "+fname
        return render(request,"age.html",{"message":"Successfull Register","age":age,"name":name,"Blood":blood})
    else:
        return render(request,"details.html",{"message":"Phone Number Is Not Coorect Plese Valide Number"})
def bar(request):
    qr=Reg.objects.filter()
    list=[]
    for i in qr:
        abc=i.blood
        list.append(abc)
    Ap=list.count("A+")
    An=list.count("A-")
    Bp=list.count("B+")
    Bn=list.count("B-")
    ABp=list.count("AB+")
    ABn=list.count("AB-")
    Op=list.count("O+")
    On=list.count("O-")
    objects = ("A+","A-","B+","B-","AB+","AB-","O+","O-")
    y_pos = np.arange(len(objects))
    performance = [Ap,An,Bp,Bn,ABp,ABn,Op,On]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Blood donor')
    plt.title('Rmd Blood Group Websites')
    plt.savefig(r"app/static/images/Barchart1.png")
    return render(request,"Barchat.html")

def search2(request):
    x=request.GET["blood"]
    qr=Reg.objects.filter(blood=x)
    return render(request,"search1.html",{"qr":qr})


def search1(request):
    return render(request,"Search1.html")


def gallery(request):
    return render(request,"Gallery.html")


def about(request):
    return render(request,"About.html")