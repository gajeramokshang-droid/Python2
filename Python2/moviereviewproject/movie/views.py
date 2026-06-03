from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from .models import Movie
def home(request):
    searchterms=request.GET.get("searchMovie")
    movies=Movie.objects.all()
    return render(request,'home.html',{'searchterms':searchterms,'movies':movies})
    

def about(request):
    return render(request,'about.html')

def singup(request):
    email = request.GET.get('email') 
    return render(request, 'signup.html', {'email': email})

