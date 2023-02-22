from django.urls import path
from .views import *

urlpatterns=[
    # path('shopregister/',shopregister),
    path('imgupload/',imgupload),
    # path('userreg/',register),
    # path('shoplogin/',login),
    # path('userlogin/',userlogin),
    path('homepage/',homepage),
    path('index/',index),
    path('menu/',menu),
    path('reg/',reg),
    path('log/',log),
    path('user/',regis),
    path('ulogin/',ulogin),
    path('pfile/',pfile),
    path('ufile/',file),
    path('dis/',dfile),
    path('delete/<int:id>',productdelete),
    path('edit/<int:id>',editproduct),
    path('verify/<auth_token>',verify), #string
    path('cart/<int:id>',addcart),
    path('upfile/',userpfile),
    path('upload/',upload),
    # path('display/',display),
    path('userprodis/',userprodisplay),
    path('cartdis/',cartdisplay),
    path('whislist/<int:id>',whis1),
    path('whisdis/',whislistdis),
    path('cartdel/<int:id>',cart_del),
    path('whishcart/<int:id>',whiscart),
    path('whishdel/<int:id>',whish_del),
    path('cartbuy/<int:id>',cart_buy),
    path('cardpay/',card_pay),
    path('cartalready',cart_al_ready),






]