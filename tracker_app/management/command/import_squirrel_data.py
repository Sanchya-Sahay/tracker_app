import csv
from django.core.management import BaseCommand
from app.models import Question

class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                squirrel = Squirrel.objects.create(
                    x=row[0]
                    y=row[1]
                    unique_squirrel_id=row[2]
                    shift=row[4]
                    date=row[5]
                    age=row[7]
                    primary_fur_color=row[8]
                    location=row[12]
                    specific_location=row[14]
                    running=row[15]
                    chasing=row[16]
                    climbing=row[17]
                    eating=row[18]
                    foraging=row[19]
                    other_activities=row[20]
                    kuks=row[21]
                    quaas=row[22]
                    moans=row[23]
                    tail_flags=row[24]
                    tail_twitches=row[25]
                    approaches=row[26]
                    indifferent=row[27]
                    runs_from=row[28]
                )
                squirrel.save()
