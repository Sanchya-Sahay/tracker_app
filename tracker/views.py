from django.shortcuts import render
from django.http import HttpResponse

def sightings(request):
    return HttpResponse("The list of squirrel sightings will go here")

def map(request):
    return HttpResponse("The squirrel map will go here")

def sighting_update(request):
    return HttpResponse ("Hi, I'm squirrel.}")

def new_sighting(request):
    return HttpResponse("Here's where we'll add a sighting!")

def stats(request): 
    return HttpResponse("Here are some stats.") 
  
# Create your views here.
