from django.shortcuts import render,redirect
from .models import Booking,Hotel
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    hotels=Hotel.objects.all()
    return render(request,"home.html",{"hotels":hotels})


def book_hotel(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)   # don’t save yet
            booking.user = request.user         # attach logged-in user
            booking.hotel = hotel               # attach selected hotel
            booking.save()                      # now save once
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'book_hotel.html', {'form': form, 'hotel': hotel})



def signup_view(request):
    if request.method=='GET':
         return render(request,'signupaccount.html',{'form':UserCreationForm})
    else:
         if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'],password= request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
