from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from django import forms
from .forms import SightingForm

def sightings(request):
    squirrels = Squirrel.objects.all()
    context={
            'squirrels':squirrels,
         }
    return render(request, 'tracker/sightings.html', context)

def sighting_update(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SightingForm(instance=squirrel)
    context = {
            'form':form,
            }
    return render(request, 'tracker/edit.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:50]
    context = {'sightings':sightings,
            }
    return render(request, 'tracker/map.html', context)

def new_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SightingForm()

    context = {
            'form':form,
            }

    return render(request, 'tracker/new.html', context)


def stats(request): 
    eating_counts = 0
    juvenile_count = 0
    adult_count = 0
    kuks_count = 0
    quaas_count = 0 
    moans_count = 0
    for s in Squirrel.objects.all(): 
        if s.eating == True: 
             eating_counts +=1 
        else: 
             pass 
        if s.age == 'Juvenile':
            juvenile_count +=1
        elif s.age == 'Adult':
            adult_count +=1
        else:
            pass
        if s.kuks == True:
            kuks_count +=1
        else:
            pass
        if s.quaas ==True:
            quaas_count +=1
        else:
            pass
        if s.moans == True:
            moans_count +=1
        else:
            pass
   
    context = {'eating_counts': eating_counts,
                'juvenile_count':juvenile_count,
                'adult_count': adult_count,
                'kuks_count':kuks_count,
                'quaas_count':quaas_count,
                'moans_count': moans_count,
            }
    return render(request, 'tracker/stats.html', context)
# Create your views here.
