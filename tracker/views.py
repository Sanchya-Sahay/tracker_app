from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from django import forms

class SightingForm(forms.Form):
    x = forms.CharField(label='X Coordinate', max_length=100, required=False)
    y = forms.CharField(label='Y Coordinate', max_length=100, required=False)
    unique_squirrel_id = forms.CharField(label='Unique Squirrel ID', max_length=100 , required=False)
    shift=forms.ChoiceField(label='Shift', choices=Squirrel.SHIFT_CHOICES, required=False)
    date= forms.IntegerField(label='Date', required=False)
    age=forms.ChoiceField(label='Age', choices=Squirrel.AGE_CHOICES, required=False)
    primary_fur_color = forms.ChoiceField(label='Primary Fur Color', choices=Squirrel.FUR_CHOICES, required=False)
    location=forms.ChoiceField(label='Location', choices=Squirrel.LOCATION_CHOICES, required=False)
    specific_location = forms.CharField(label='Specific Location', max_length=255, required=False)
    running = forms.BooleanField(label="Running", required=False)
    chasing = forms.BooleanField(label="Chasing", required=False)
    climbing = forms.BooleanField(label="Climbing", required=False)
    eating = forms.BooleanField(label="Eating", required=False)
    foraging = forms.BooleanField(label="Foraging", required=False)
    other_activities = forms.CharField(label="Other Activities" , max_length=255, required=False)
    kuks = forms.BooleanField(label="Kuks", required=False)
    quaas = forms.BooleanField(label="Quaas", required=False)
    moans = forms.BooleanField(label="Moans", required=False)
    tail_flags = forms.BooleanField(label="Tail Flags", required=False)
    tail_twitches = forms.BooleanField(label="Tail Twitches", required=False)
    approaches = forms.BooleanField(label="Approaches", required=False)
    indifferent = forms.BooleanField(label="Indifferent", required=False)
    runs_from = forms.BooleanField(label="Runs From", required=False)

def sightings(request):
    squirrels = Squirrel.objects.all()
    context={
            'squirrels':squirrels,
         }
    return render(request, 'tracker/sightings.html', context)

def sighting_update(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Invalid form response")

        squirrel.x = form.cleaned_data['x']
        squirrel.y = form.cleaned_data['y']
        # will not edit squirrel id here
        squirrel.shift=form.cleaned_data['shift']
        squirrel.date=form.cleaned_data['date']
        squirrel.age=form.cleaned_data['age']
        squirrel.primary_fur_color = form.cleaned_data['primary_fur_color']
        squirrel.location= form.cleaned_data['location']
        squirrel.specific_location =form.cleaned_data['specific_location']
        squirrel.running = form.cleaned_data['running']
        squirrel.chasing = form.cleaned_data['chasing']
        squirrel.climbing = form.cleaned_data['climbing'] 
        squirrel.eating = form.cleaned_data['eating']
        squirrel.foraging = form.cleaned_data['foraging'] 
        squirrel.other_activities = form.cleaned_data['other_activities']
        squirrel.kuks = form.cleaned_data['kuks'] 
        squirrel.quaas = form.cleaned_data['quaas'] 
        squirrel.moans = form.cleaned_data['moans'] 
        squirrel.tail_flags = form.cleaned_data['tail_flags']
        squirrel.tail_twitches = form.cleaned_data['tail_twitches'] 
        squirrel.approaches = form.cleaned_data['approaches'] 
        squirrel.indifferent = form.cleaned_data['indifferent'] 
        squirrel.runs_from = form.cleaned_data['runs_from'] 
        squirrel.save()

    elif request.method == 'DELETE':
        squirrel.delete()
        return redirect('/sightings/')

    context = {
        'sighting': squirrel,
        'form': SightingForm(initial={
            'x': squirrel.x,
            'y': squirrel.y,
            'unique_squirrel_id': squirrel.unique_squirrel_id,
            'shift':squirrel.shift,
            'date':squirrel.date,
            'age':squirrel.age,
            'primary_fur_color': squirrel.primary_fur_color,
            'location':squirrel.location,
            'specific_location':squirrel.specific_location,
            'running':squirrel.running,
            'chasing':squirrel.chasing,
            'climbing':squirrel.climbing,
            'eating':squirrel.eating,
            'foraging':squirrel.foraging,
            'other_activities':squirrel.other_activities,
            'kuks':squirrel.kuks,
            'quaas':squirrel.quaas,
            'moans':squirrel.moans,
            'tail_flags':squirrel.tail_flags,
            'tail_twitches':squirrel.tail_twitches,
            'approaches':squirrel.approaches,
            'indifferent':squirrel.indifferent,
            'runs_from':squirrel.runs_from,
        })
    }
    return render(request, 'tracker/edit.html', context)

def map(request):
    return HttpResponse("The squirrel map will go here")


def new_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Invalid form response")

        squirrel = Squirrel.objects.create(unique_squirrel_id=form.cleaned_data['unique_squirrel_id'])
        squirrel.x = form.cleaned_data['x']
        squirrel.y = form.cleaned_data['y']
        squirrel.shift=form.cleaned_data['shift']
        squirrel.date=form.cleaned_data['date']
        squirrel.age=form.cleaned_data['age']
        squirrel.primary_fur_color = form.cleaned_data['primary_fur_color']
        squirrel.location= form.cleaned_data['location']
        squirrel.specific_location =form.cleaned_data['specific_location']
        squirrel.running = form.cleaned_data['running']
        squirrel.chasing = form.cleaned_data['chasing']
        squirrel.climbing = form.cleaned_data['climbing']
        squirrel.eating = form.cleaned_data['eating']
        squirrel.foraging = form.cleaned_data['foraging']
        squirrel.other_activities = form.cleaned_data['other_activities']
        squirrel.kuks = form.cleaned_data['kuks']
        squirrel.quaas = form.cleaned_data['quaas']
        squirrel.moans = form.cleaned_data['moans']
        squirrel.tail_flags = form.cleaned_data['tail_flags']
        squirrel.tail_twitches = form.cleaned_data['tail_twitches']
        squirrel.approaches = form.cleaned_data['approaches']
        squirrel.indifferent = form.cleaned_data['indifferent']
        squirrel.runs_from = form.cleaned_data['runs_from']
        # add here
        squirrel.save()

        return redirect('/sightings/' + squirrel.unique_squirrel_id +  '/')

    context = {
        'form': SightingForm()
    }
    return render(request, 'tracker/new.html', context)

def stats(request): 
    return HttpResponse("Here are some stats.") 
  
# Create your views here.
