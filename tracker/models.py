from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x = models.DecimalField(
             blank=True,
             max_digits=21,
             decimal_places=21,
             null=True,
             )
    y = models.DecimalField(
            blank=True,
            max_digits=21,
            decimal_places=21,
            null=True,
            )
    unique_squirrel_id = models.CharField(
           primary_key=True,
           max_length=15,
           )
    hectare = models.CharField(
            blank=True,
            max_length=3,
            )
    AM = 'am'
    PM = 'pm'

    SHIFT_CHOICES = (
            (AM, 'am'),
            (PM, 'pm'),
            )
    shift = models.CharField(
            choices = SHIFT_CHOICES,
            blank=True,
            max_length=2,
            )
    date = models.CharField(
            blank=True,
            max_length=8,
            )
    hectare_squirrel_number = models.IntegerField(
            blank=True,
            null=True,
            )
    ADULT = 'adult'
    JUVENILE = 'juvenile'

    AGE_CHOICES = (
            (ADULT, 'adult'),
            (JUVENILE, 'juvenile'),
            )

    age = models.CharField(
            choices = AGE_CHOICES,
            blank=True,
            max_length=10,
            )

    GRAY = 'gray'
    CINNAMON = 'cinnamon'
    BLACK  ='black'

    FUR_CHOICES = (
            (GRAY,'gray'),
            (CINNAMON, 'cinnamon'),
            (BLACK, 'black'),
            )

    primary_fur_color = models.CharField(
            choices = FUR_CHOICES,
            blank=True,
            max_length=10,
            )

    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'

    LOCATION_CHOICES =(
            (GROUND_PLANE, 'ground plane'),
            (ABOVE_GROUND, 'above ground')
            )

    location = models.CharField(
            choices = LOCATION_CHOICES,
            blank=True,
            max_length=20,
            )

    specific_location = models.CharField(
            blank=True,
            max_length=255,
            )

    running = models.BooleanField(
            null=True,
            )
   
    chasing = models.BooleanField(
            null=True,
            )
    
    climbing = models.BooleanField(
            null=True,
            )

    eating = models.BooleanField(
            null=True,
            )

    foraging = models.BooleanField(
            null=True,
            )

    other_acivities = models.CharField(
            blank=True,
            max_length=255,
            )

    kuks = models.BooleanField(
            null=True,
            )

    quaas = models.BooleanField(
            null=True,
            )

    moans = models.BooleanField(
            null=True,
            )
    
    tail_flags = models.BooleanField(
            null=True,
            )
    
    tail_twitches = models.BooleanField(
            null=True,
            )

    approaches = models.BooleanField(
            null=True,
            )

    indifferent = models.BooleanField(
            null=True,
            )

    runs_from = models.BooleanField(
            null=True,
            )
# Create your models here.
