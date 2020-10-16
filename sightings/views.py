from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

def index(request):
    Sightings=Squirrel.objects.all()
    context={'sightings':Sightings,}
    return render (request, 'sightings/index.html',context)

def details(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            context={'sightings':Squirrel.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
        form = SquirrelForm()
    context = {'form':form}
    return render(request, 'sightings/update.html',context)

def update(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=Sightings)
        if form.is_valid():
            form.save()
            context={'squirrel':Squirrel.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
        form = SquirrelForm(instance=Sightings)
    context = {'form':form}
    return render(request, 'sightings/update.html',context)

