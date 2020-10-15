from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def index(request):
    Sightings=Squirrel.objects.all()
    context={'sightings':Sightings,}
    return render (request, 'sightings/index.html',context)
