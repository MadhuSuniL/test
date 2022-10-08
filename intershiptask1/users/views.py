from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def loginpage(req):
    return render(req, 'login.html')
    
def home(req):
    if str(req.user) != "AnonymousUser":
        return render(req, 'home.html')
    else:
        messages.error(req, "Error : User Not Found..!")
        return redirect('/user')
        

def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            messages.success(req, "Success : Logged In Successfully...")
            return redirect('/user/home')
        else:
            messages.error(req, "User Not Found..!")
            return redirect('/user')
    return render(req, '/user')

def newlogin_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        password2 = req.POST['password2']
        email = req.POST['email']
        if password != password2:
            messages.error(req, "Warning :Password Should be matched...")
            return redirect('/user/newlogin')
        User.objects.create_user(username=username,password=password,email=email)
        messages.success(req, 'Success : Account Created Successfully.. Please Login Now...!')
        return redirect('/user')
    return render(req, 'newlogin.html')




def logout_user(req):
    logout(req)
    messages.success(req, 'Success : Logged Out Successfully..!')        
    return redirect('/user')
    
                        