import os

from django.contrib.auth import authenticate
from django.core.mail import send_mail
from newproject.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.contrib.auth import authenticate
import datetime
from datetime import timedelta


# Create your views here.
# def shopregister(request):
#     if request.method=='POST':
#         a=shpregform(request.POST)
#         if a.is_valid():
#             sm=a.cleaned_data["Shop_Name"]
#             em=a.cleaned_data["Email_id"]
#             ph=a.cleaned_data["Phone_Num"]
#             ad=a.cleaned_data["Address"]
#             sid=a.cleaned_data["Shop_id"]
#             ps=a.cleaned_data["password"]
#             cp=a.cleaned_data["Confirm_Password"]
#             if ps==cp:
#                 b=shpregmodel(Shop_Name=sm,Email_id=em,Phone_Num=ph,Address=ad,Shop_id=sid,password=ps)
#                 b.save()
#                 return HttpResponse("registration success")
#             else:
#                 return HttpResponse("password dosnt match")
#         else:
#             return HttpResponse("registration failed")
#     return render(request,'shopregister.html')
def imgupload(request):
    if request.method=='POST':
        a=imageform(request.POST,request.FILES)
        if a.is_valid():

            fl=a.cleaned_data['imgfile']
            b=imagemodel(imgfile=fl)
            b.save()
            return HttpResponse("image upload successfully")
        else:
            return HttpResponse('upload failed')
    return render(request,'imageupload.html')
# def register(request):
#     if request.method=='POST':
#         a=regform(request.POST)
#         if a.is_valid():
#             nm=a.cleaned_data["name"]
#             em=a.cleaned_data["email"]
#             ph=a.cleaned_data["phone"]
#             ad=a.cleaned_data["address"]
#             pi=a.cleaned_data["pincode"]
#             ps=a.cleaned_data["password"]
#             cp=a.cleaned_data["cnfmpassword"]
#             if ps==cp:
#                 b=regmodel(name=nm,email=em,phone=ph,address=ad,pincode=pi,password=ps)
#                 b.save()
#                 return HttpResponse("registration success")
#             else:
#                 return HttpResponse("password doesnt match")
#         else:
#             return HttpResponse("registration failed")
#     return render(request,'userregister.html')
# def login (request):
#     if request.method=='POST':
#         a=shplogform(request.POST)
#         if a.is_valid():
#             sm=a.cleaned_data["Shop_Name"]
#             ps=a.cleaned_data["password"]
#             b=shpregmodel.objects.all()
#             for i in b:
#                 if sm==i.Shop_Name and ps==i.password:
#                     return HttpResponse("login success")
#             else:
#                 return HttpResponse("login failed")
#     return render(request,'login.html')
# def userlogin(request):
#     return render(request,'userlogin.html')
# def homepage(request):
#     return render(request,'homepage.html')

def index(request):
    return render(request,'indexpage.html')
def menu(request):
    return render(request,'menupage.html')
def reg(request):
    if request.method=='POST':
        a=registerform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["name"]
            pl=a.cleaned_data["place"]
            sp=a.cleaned_data["shop_id"]
            em=a.cleaned_data["email"]
            ps=a.cleaned_data["password"]
            cp=a.cleaned_data["conpassword"]
            if ps==cp:
                b=registermodel(name=us,place=pl,shop_id=sp,email=em,password=ps)
                b.save()
                return redirect(log)
            else:
                return HttpResponse("password doesn't match")
        else:
            return HttpResponse("fail")
    return render(request,'shop_register.html')
def log(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["name"]
            ps=a.cleaned_data["password"]
            b=registermodel.objects.all()
            for i in b:
                if us==i.name and ps==i.password:
                    return redirect(pfile)
            else:
                return HttpResponse("login Failed")
    return render(request,'shop_login.html')



def pfile(request):
    return render(request,'profile.html')
# def upload(request):
#     return render(request,'fileupload.html')
# def display(request):
#     a = ufilemodel.objects.all()
#     image = []
#     name = []
#     price = []
#     id = []
#     for i in a:
#         id1 = i.id
#         id.append(id1)
#         im = i.imgfile
#         image.append(str(im).split('/')[-1])
#         nm = i.prdctname
#         name.append(nm)
#         pr = i.prdctprice
#         price.append(pr)
#     mylist = zip(image, name, price, id)
#     return render(request, 'filedisplay.html', {'mylist': mylist})
def file(request):
    if request.method=='POST':
        a=ufileform(request.POST,request.FILES)
        if a.is_valid():
            pn=a.cleaned_data['prdctname']
            pp=a.cleaned_data['prdctprice']
            fl=a.cleaned_data['imgfile']
            b=ufilemodel(prdctname=pn,prdctprice=pp,imgfile=fl)
            b.save()
            return HttpResponse("file upload successfully")
        else:
            return HttpResponse('upload failed')
    return render(request,'fileupload.html')
def dfile(request):
    a =ufilemodel.objects.all()
    image = []
    name = []
    price=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        im = i.imgfile
        image.append(str(im).split('/')[-1])
        nm = i.prdctname
        name.append(nm)
        pr=i.prdctprice
        price.append(pr)
    mylist = zip(image, name,price,id)
    return render(request,'filedisplay.html',{'mylist':mylist})
def productdelete(request,id):
    a=ufilemodel.objects.get(id=id)
    a.delete()
    return redirect(dfile)
def editproduct(request,id):
    a=ufilemodel.objects.get(id=id)
    im=str(a.imgfile).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES):
            if len(a.imgfile)>0:
                os.remove(a.imgfile.path)
            a.imgfile=request.FILES['imgfile']
        a.prdctname=request.POST.get('prdctname')
        a.prdctprice=request.POST.get("prdctprice")
        a.save()
        return redirect(dfile)

    return render(request,'editfile.html',{'a':a,'im':im})
def regis(request):
    if request.method=='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).first():
            # it will get frst object from filter query
            # msg.success is a framewrk that allows u to stre msges in one rqst nd retrive them in the rqst pge
            messages.success(request,'username already taken')
            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)
        user_obj=User(username=username,email=email,first_name=first_name,last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        # uuid module-uuid thats for universally unique identifiers
        # uuid4() create random uuid
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        # userdefined fun
        send_mail_regis(email,auth_token)  #mail sending function
        return render(request,'ereg.html')
    return render(request,'userregister.html')

def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'click the link to verify your account http://127.0.0.1:8000/myapp/verify/{auth_token}'
    email_from=EMAIL_HOST_USER #from
    recipient=[email] #to
    # inbuild fun
    send_mail(subject,message,email_from,recipient)
def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(ulogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(ulogin)
    else:
        messages.success(request,"user not found")
        return redirect(ulogin)

def ulogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(ulogin)
        profile_obj=profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your mail')
            return redirect(ulogin)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(ulogin)
        return redirect(userpfile)
    return render(request,'userlogin.html')
def userpfile(request):
    return render(request,'userprofile.html')

def userprodisplay(request):
    a = ufilemodel.objects.all()
    image = []
    name = []
    price = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        im = i.imgfile
        image.append(str(im).split('/')[-1])
        nm = i.prdctname
        name.append(nm)
        pr = i.prdctprice
        price.append(pr)
    mylist = zip(image, name, price, id)
    return render(request,'userprodis.html', {'mylist': mylist})


def addcart(request,id):
    a=ufilemodel.objects.get(id=id)
    if cart.objects.filter(prdctname=a.prdctname):
        messages.success(request,'already added')
        return redirect(cart_al_ready)
    b=cart(prdctname=a.prdctname,prdctprice=a.prdctprice,imgfile=a.imgfile)
    b.save()
    return redirect(cartdisplay)
def cart_al_ready(request):
    return render(request,'cart_already_added.html')


def cartdisplay(request):
    a = cart.objects.all()
    image = []
    name = []
    price = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        im = i.imgfile
        image.append(str(im).split('/')[-1])
        nm = i.prdctname
        name.append(nm)
        pr = i.prdctprice
        price.append(pr)
    mylist = zip(image, name, price, id)
    return render(request, 'cart.html', {'mylist': mylist})

def whis1(request,id):
    a = ufilemodel.objects.get(id=id)
    if whislist.objects.filter(prdctname=a.prdctname):
        messages.success(request, 'already added')
        return redirect(wish_al_ready)
    b = whislist(prdctname=a.prdctname, prdctprice=a.prdctprice, imgfile=a.imgfile)
    b.save()
    # return HttpResponse('added')
    return redirect(whislistdis)
def wish_al_ready(request):
    return render(request,"wish_already_added.html")



def whislistdis(request):
    a = whislist.objects.all()
    image = []
    name = []
    price = []
    id = []
    for i in a:
        id1=i.id
        id.append(id1)
        im=i.imgfile
        image.append(str(im).split('/')[-1])
        nm=i.prdctname
        name.append(nm)
        pr=i.prdctprice
        price.append(pr)
    mylist=zip(image,name,price,id)
    print(name)
    return render(request,'whislist.html',{'mylist':mylist})


def whiscart(request,id):
    a=whislist.objects.get(id=id)
    if cart.objects.filter(prdctname=a.prdctname):
        messages.success(request, 'already added')
        return redirect(wishcart_al_ready)
    b=cart(prdctname=a.prdctname,prdctprice=a.prdctprice,imgfile=a.imgfile)
    b.save()
    return redirect(whislistdis)
def wishcart_al_ready(request):
    return render(request,"wish_cart_already_added.html")
def whish_del(request,id):
    a=whislist.objects.get(id=id)
    a.delete()
    return redirect(whislistdis)


def cart_del(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)


def cart_buy(request,id):
    a=cart.objects.get(id=id)
    im=str(a.imgfile).split('/')[-1]
    if request.method=='POST':
        prdctname=request.POST.get('prdctname')
        prdctprice=request.POST.get('prdctprice')
        quantity=request.POST.get('quantity')
        b=buy(prdctname=prdctname,prdctprice=prdctprice,quantity=quantity)
        b.save()
        total=int(prdctprice)*int(quantity)
        return render(request,'final_bill.html',{'b':b,'tt':total})
    return render(request,'buypro.html',{'a':a ,'im':im})
def card_pay(request):
    if request.method=='POST':
        cardname=request.POST.get('cardname')
        cardnumber=request.POST.get('cardnumber')
        cardexpiry=request.POST.get('cardexpiry')
        code=request.POST.get('code')
        user_obj=customercard(cardname=cardnumber,cardnumber=cardnumber,cardexpiry=cardexpiry,code=code)
        user_obj.save()
        today=datetime.date.today()
        today+=timedelta(days=10)
        return render(request,"success.html",{'date':today})
    return render(request,'card_payment.html')
