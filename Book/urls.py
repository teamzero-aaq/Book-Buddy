from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from . import deleteall

urlpatterns = [
  #  path('home/',views.home),
   # path('',views.home),
    path('login/',views.login),
    path('verify/',views.verify),
    path('Signup/',views.register),
    #path('deleteall/',deleteall.dele),
    path('useradd/',views.adduser),
    path('forgot/',views.forgotpass),
    path('reset/',views.resetpass),
    path('addbook/',views.addBook),
    path('addbookdb/',views.addBookdb),
    path('viewbook/',views.viewbook),
    path('logout/',views.userlogout),
    path('testbook/',views.usertestBook),
    path('dashboard/',views.dashboard),
    url(r'^book/(?P<pk>\d+)/$', views.usertestBook),

]