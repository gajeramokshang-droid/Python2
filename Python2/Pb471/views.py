
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# Signup view 
def signup_view(request):
    if request.method=='GET':
         return render(request,'signupaccount.html',{'form':UserCreationForm})
    else:
         if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'],password= request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')

# Logout view
def logout_view(request):
    logout(request)
    return render(request, "logout.html")

