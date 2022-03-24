# Create your views here.
from django.shortcuts import redirect, render
from .forms import MyUserCreationForm
from django.contrib import messages


def registration(req):
    if req.method=='POST':
        form = MyUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Congratulations, your account has been successfully created. Please Login.')
            return redirect('login')
    elif req.method=='GET':
        form = MyUserCreationForm()
    data = {'form':form}
    return render(req,'accounts/registration.html', data )

from .forms import MyAuthenticationForm
from django.contrib.auth import authenticate,login,logout
def mylogin(req):
    if req.method=='GET':
        form = MyAuthenticationForm()
    elif req.method=='POST':
        form = MyAuthenticationForm(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            # messages.success(req,'Login Successfull.')
            return render(req,'webapp/home.html')
        else:
            messages.error(req,'Invalid Username or Password') 
    data = {'form':form}
    return render(req,'accounts/login.html',data)

def mylogout(req):
    logout(req)
    messages.success(req,'Logout Successfully....')
    return redirect('login')