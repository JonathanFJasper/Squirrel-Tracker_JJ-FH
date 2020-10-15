from django.shortcuts import render
from sightings.models import Squirrel

def index(request):
    sightings = Squirrel.objects.all()[:98]
    context = {'sightings': sightings,}
    return render(request, 'map/index.html', context)
        

