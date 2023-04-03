from django import forms

class imageform(forms.Form):

    imgfile=forms.ImageField()

class shpregform(forms.Form):
    Shop_Name=forms.CharField(max_length=30)
    Email_id=forms.EmailField()
    Phone_Num=forms.IntegerField()
    Address=forms.CharField(max_length=30)
    Shop_id=forms.IntegerField()
    password=forms.CharField(max_length=20)
    Confirm_Password=forms.CharField(max_length=20)
class shplogform(forms.Form):
    Shop_Name=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)
class regform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=20)
    pincode=forms.IntegerField()
    password=forms.CharField(max_length=20)
    cnfmpassword=forms.CharField(max_length=20)
class registerform(forms.Form):
    name = forms.CharField(max_length=20)
    place = forms.CharField(max_length=20)
    shop_id = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    conpassword = forms.CharField(max_length=20)
class loginform(forms.Form):
    name = forms.CharField(max_length=20)

    password = forms.CharField(max_length=20)



class ufileform(forms.Form):
    prdctname=forms.CharField(max_length=20)
    prdctprice=forms.IntegerField()
    imgfile=forms.ImageField()

class customercardform(forms.Form):
    cardname=forms.CharField(max_length=30)
    cardnumber=forms.CharField(max_length=30)
    cardexpiry=forms.CharField(max_length=30)
    code=forms.CharField(max_length=30)

