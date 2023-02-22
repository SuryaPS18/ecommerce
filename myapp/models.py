from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class imagemodel(models.Model):

    imgfile=models.ImageField(upload_to='myapp/static')

class shpregmodel(models.Model):
    Shop_Name=models.CharField(max_length=30)
    Email_id=models.EmailField()
    Phone_Num=models.IntegerField()
    Address=models.CharField(max_length=30)
    Shop_id=models.IntegerField()
    password=models.CharField(max_length=20)
class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=20)
    pincode=models.IntegerField()
    password=models.CharField(max_length=20)
class registermodel(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    shop_id = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
class uregmodel(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
class ufilemodel(models.Model):
    prdctname=models.CharField(max_length=20)
    prdctprice=models.IntegerField()
    imgfile=models.ImageField(upload_to='myapp/static')
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
class cart(models.Model):
    prdctname = models.CharField(max_length=20)
    prdctprice = models.IntegerField()
    imgfile = models.ImageField()
class whislist(models.Model):
    prdctname = models.CharField(max_length=20)
    prdctprice = models.IntegerField()
    imgfile = models.ImageField()
class buy(models.Model):
    prdctname = models.CharField(max_length=20)
    prdctprice = models.IntegerField()
    quantity=models.IntegerField()
class customercard(models.Model):
    cardname=models.CharField(max_length=30)
    cardnumber=models.IntegerField()
    cardexpiry=models.DateTimeField()
    code=models.IntegerField()


