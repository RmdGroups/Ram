from django.db import models
class Register(models.Model):
    idno=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)


class Reg(models.Model):
    idno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    blood=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    mandal=models.CharField(max_length=30)
    village=models.CharField(max_length=30)

