from django.shortcuts import render,redirect,get_object_or_404
from .models import Player
def home(request):
    players=Player.objects.all()
    return render(request,'home.html',{'players':players})

def welcome(request):
    return render(request,'welcome.html')

def add_player(request):
    if request.method=="POST":
        name=request.POST.get('name')
        innings=request.POST.get("innings")
        runs=request.POST.get("runs")

        Player.objects.create(name=name,test_innings=innings,runs=runs)
        return redirect('home')
    return render(request,'add_player.html')

def edit_player(request,player_id):
    player=get_object_or_404(Player,pk=player_id)
    if request.method=="GET":
        return render(request,'edit_player.html',{"player":player})
    else:
        player.name=request.POST.get('name')
        player.test_innings=request.POST.get('innings')
        player.runs=request.POST.get('runs')
        player.save()
        return redirect('home')

def delete_player(request,player_id):
    player=get_object_or_404(Player,pk=player_id)
    player.delete()
    return redirect('')        