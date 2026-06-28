from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
def signup(request):
    if(request.method=='GET'):
        return render(request,'home.html',{"forms":UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            form=User.objects.create_user(request.POST['username'],data=request.POST['password1'])
            form.save()
            login(request,form)
            return redirect("home")
        
