# Browser URL → urls.py (path) → views.py (function) → template.html (page shown)

from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout

def signup_view(request):
    if request.method=='GET':
        return render(request,'signup.html',{"form":UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(request.POST['username'],data=request.POST['password'])
            user.save()
            login(request,user)
            return redirect('home')
        
def login_view(request):
    if request.method=="POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect('home')