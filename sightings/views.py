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
        form = SquirrelForm(request.POST, instance=Squirrel)
        if form.is_valid():
            form.save()
            context={'squirrel':Squirrel.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
        form = SquirrelForm(instance=Squirrel)
    context = {'form':form}
    return render(request, 'sightings/update.html',context)

def stats(request):
    s1 = sightings.objects.all().count()
    s2 = sightings.objects.filter(Shift='AM').count()
    s3 = sightings.objects.filter(Primary_Fur_Color='Gray').count()
    s4 = sightings.objects.filter(Eating = True).count()
    s5 = sightings.objects.filter(Age = 'Juvenile').count()
    
    context={'s1':s1, 's2':s2, 's3':s3, 's4':s4, 's5':s5,}
    
    return render(request, 'sightings/stats.html', context)    