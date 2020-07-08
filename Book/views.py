from django.shortcuts import render
from django.http import HttpResponse
from .TestFire import   getdb,getstore
import uuid
from .Common import CUser
import time


#from BookBuddy.Common.TestFire import getdb
#Create your views here.

def login(request):
    c={}
    return render(request,'Login.html',c)

def register(req):
    return render(req,'signup.html',{})

def forgotpass(req):
    return render(req,'forget.html',{})

def resetpass(req):
    return render(req,'reset.html',{})

def addBook(req):
    if CUser.isLogin:
        return render(req, 'addbook.html', {})
    else:
        return render(req, 'login.html', {})
def dashboard(req):
    if CUser.isLogin:
        c = {'user': CUser.currentuser.val()}
        return render(req, 'cong.html',c)
    else:
        return render(req, 'login.html', {})

def verify(request):

    if not CUser.isLogin:
        mail=request.POST.get('mail')
        password=request.POST.get('password')
    
        db=getdb()
        user=db.child("users").child(mail).get()
 
        if not user.val():
            return HttpResponse("User does not exist")
        elif (password==user.val().get("password")):
            c={'user':user.val()}
            CUser.currentuser=user
      
            CUser.isLogin=True
            return render(request, 'cong.html', c)
        else:
            return HttpResponse("Wrong password")
    else:
        c = {'user': CUser.currentuser.val()}
        return render(request, 'cong.html', c)
 
def userlogout(req):
    CUser.isLogin=False
    return render(req, 'login.html', {})

def addBookdb(req):


    if CUser.isLogin:

        bname = req.POST['bookname']
        publication = req.POST['bpublication']
        author = req.POST['bauthor']
        description = req.POST['bdescription']
        phone1 = req.POST['phone1']
        price = req.POST['bprice']
        cat1 = req.POST['bcat1']
        cat2 = req.POST['bcat2']
        path = req.POST['imgpath']



        bookid = str(time.time())
        bookid=bookid.replace(".","")
        phone = CUser.currentuser.val().get("phone")
        uname = CUser.currentuser.val().get("name")
        imgid = uuid.uuid4().hex


        imgpath = r'C:\Users\Public\Pictures\Sample Pictures\Chrysanthemum.jpg'
        db = getdb()
        storage = getstore()

        storage.child("BookImages").child(imgid).put(path)
        imgurl = storage.child("BookImages").child(imgid).get_url(1)
 

        data = {"name": bname, "publication": publication, "author": author,
                "description": description, "phone1": phone1, "price": price, "bookcat": cat1,
                "booktype": cat2, "userphone": phone,"bookimg":imgurl,"username":uname}

        db.child("bookbuddybook").child(bookid).set(data)

        c = {'user': CUser.currentuser.val()}
        return render(req,'cong.html',c)
    else:
        return render(req, 'login.html', {})

def adduser(req):
    name=req.POST['name']
    email=req.POST['email']
    phone=req.POST['phone']
    address=req.POST['address']
    passwrd=req.POST['pass']
    cpasswrd=req.POST['passc']
    stream=req.POST['Streams']

    if(passwrd!=cpasswrd):
        return HttpResponse("Password Not match")
    else:
       
        db=getdb()
        user = db.child("users").child(phone).get()

        if  user.val():
            return HttpResponse("User exist")
        else:
            data = {
                "name": name,"mail":email,"password":passwrd,"phone":phone,"address":address,"stream":stream
             }
            db.child("users").child(phone).set(data)
        
            return render(req,'Login.html',{})

def viewbook(req):
    db = getdb()
    allbooks = db.child("bookbuddybook").order_by_key().get()

    allbook={'books':allbooks.val()}

    return render(req,'booklist.html',allbook)

def usertestBook(req,pk):
    db = getdb()
    currentBook = db.child("bookbuddybook").child(str(pk)).get()

    book={"book":currentBook.val()}
    return render(req,'viewbook.html',book)