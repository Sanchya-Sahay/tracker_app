import csv
from django.db import IntegrityError
from django.core.management import BaseCommand
from tracker.models import Squirrel
import argparse

class Command(BaseCommand):
    help = 'Export sightings to CSV'
    
    def add_arguments(self,parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'w') as f:
            writer = csv.writer(f, dialect='excel')
            for squirrel in Squirrel.objects.all():
                writer.writerow([
                    squirrel.x,
                    squirrel.y,
                    squirrel.unique_squirrel_id,
                    squirrel.shift,
                    squirrel.date,
                    squirrel.age,
                    squirrel.primary_fur_color,
                    squirrel.location,
                    squirrel.specific_location,
                    squirrel.running,
                    squirrel.chasing,
                    squirrel.climbing,
                    squirrel.eating,
                    squirrel.foraging,
                    squirrel.other_activities,
                    squirrel.kuks,
                    squirrel.quaas,
                    squirrel.moans,
                    squirrel.tail_flags,
                    squirrel.tail_twitches,
                    squirrel.approaches,
                    squirrel.indifferent, 
                    squirrel.runs_from
                    ])

