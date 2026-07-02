from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import Cricket

def home(request):
    players=Cricket.objects.all()
    return render(request,'home.html',{'players':players})

def player_detail(request,player_id):
    user=get_object_or_404(Cricket,pk=player_id)
    if request.method=="GET":
        return render(request,'player_detail.html',{'form':user})

def add_player(request):
    if request.method=="GET":
        return render(request,'add_player.html')
    else:
        name=request.POST.get('name')
        country=request.POST.get('country')
        age=request.POST.get('age')
        batting=request.POST.get('batting')
        wickets=request.POST.get('wickets')
        bowling=request.POST.get('bowling')
        runs=request.POST.get('runs')

        Cricket.objects.create(name=name,country=country,age=age,batting=batting,wickets=wickets,bowling=bowling,runs=runs)
        return redirect('home')
   