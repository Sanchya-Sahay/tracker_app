from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def sightings(request):
    squirrels = Squirrel.objects.all()
    context={
            'squirrels':squirrels,
         }
    return render(request, 'tracker/sightings.html', context)



def map(request):
    return HttpResponse("The squirrel map will go here")

def sighting_update(request, unique_squirrel_id):
    return HttpResponse ("Hi, I'm squirrel.}")

def new_sighting(request):
    return HttpResponse("Here's where a new sighting!")

def stats(request): 
    return HttpResponse("Here are some stats.") 
  
# Create your views here.
