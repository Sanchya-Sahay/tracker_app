from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    x = models.CharField(
            blank=True,
            max_length=21,
             )
    y = models.CharField(
            blank=True,
            max_length=21,
            )
    unique_squirrel_id = models.CharField(
           primary_key=True,
           max_length=15,
           )
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            )
    shift = models.CharField(
            choices = SHIFT_CHOICES,
            blank=True,
            max_length=2,
            )
    date = models.IntegerField(
            null=True, blank=True,
            )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            )

    age = models.CharField(
            choices = AGE_CHOICES,
            blank=True,
            max_length=10,
            )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK  ='Black'

    FUR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )

    primary_fur_color = models.CharField(
            choices = FUR_CHOICES,
            blank=True,
            max_length=10,
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES =(
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground')
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
            default=False)

    chasing = models.BooleanField(
            default=False)

    climbing = models.BooleanField(
            default=False)

    eating = models.BooleanField(
            default=False)    

    foraging = models.BooleanField(
            default=False) 

    other_activities = models.CharField(
            blank=True,
            max_length=255,
            )

    kuks = models.BooleanField(
            default=False) 

    quaas = models.BooleanField(
            default=False)
            

    moans = models.BooleanField(
            default=False)
        
    
    tail_flags = models.BooleanField(
            default=False)
        
    
    tail_twitches = models.BooleanField(
            default=False)
            

    approaches = models.BooleanField(
           default=False) 
        

    indifferent = models.BooleanField(
            default=False) 
            

    runs_from = models.BooleanField(
            default=False)
            
    def __str__(self):
        return self.unique_squirrel_id
