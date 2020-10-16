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
    squirrel_data = Squirrel.objects.all()
    s1 = len(squirrel_data)
    s2 = squirrel_data.aggregate(min_latitude = Min('X'),max_latitude = Max('X'), average_latitude = Avg('X'))
    s3 = squirrel_data.aggregate(min_longitude = Min('Y'),max_longitude=Max('Y'), average_longitude = Avg('Y'))
    s4 = list(squirrel_data.values_list('Shift').annotate(Count('shift')))
    s5 = list(squirrel_data.values_list('Age').annotate(Count('age')))
    s6 = list(squirrel_data.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
    return render(request, 'sightings/stats.html', {"s1":s1, "s2":s2, "s3":s3, "s4":s4, "s5":s5, "s6":s6})