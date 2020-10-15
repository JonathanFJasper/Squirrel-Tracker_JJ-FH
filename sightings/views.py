from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def index(request):
    Sightings=Squirrel.objects.all()
    context={'sightings':Sightings,}
    return render (request, 'sightings/index.html',context)

def details(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)
