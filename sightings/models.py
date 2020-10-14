from django.db import models
from django.utils.translation import gettext as _

class Sightings(models.Model):
    Lattitude = models.DecimalField(
            max_length=100, 
            decimal_places=13, 
            help_text=_('Lattitude of sighting location'))

    Longitude = models.DecimalField(
            max_length=100,
            decimal_places=13,
            help_text=_('Longitude of sighting location'))

    Unique_Squirrel_ID= models.CharField(
            max_length=100,
            help_text=_('Unique ID of the squirrel sighted'))

    AM = 'am'
    PM = 'pm'
   
    SHIFT_CHOICES = [
            (PM,_('PM')),
            (AM,_('AM')),
            ]

    Shift = models.CharField(
            max_length=15,
            help_text=_('Shift of Sighting'),
            choices=SHIFT_CHOICES,
            default=AM,
            )

    Date = models.DateField(
            help_text=_('Date of sighting'),
            )

    JUVENILE  = 'juvenile'
    ADULT = 'adult'
    OTHER = 'Other'

    AGE_CHOICES = [
            (JUVENILE,_('Juvenile')),
            (ADULT,_('Adult')),
            (OTHER,_('Other')),
            ]

    Age = models.CharField(
            max_length=15,
            help_text=_('Age of Squirrel'),
            choices=AGE_CHOICES,
            default=OTHER,
            blank=True, 
            )

    BLACK  = 'black'
    CINNAMON = 'cinnamon'
    GRAY = 'gray'
    OTHER = 'other'

    PRIMARY_FUR_COLOR_CHOICES = [
            (BLACK,_('Black')),
            (CINNAMON,_('Cinnamon')),
            (GRAY,_('Gray')),
            (OTHER,_('Other')),
            ]

    Primary_Fur_Color = models.CharField(
            max_length=50,
            help_text=_('Color of Squirrel'),
            choices=PRIMARY_FUR_COLOR_CHOICES,
            default=OTHER,
            blank=True,
            )

    GROUND_PLANE  = 'ground plane'
    ABOVE_GROUND  = 'above ground'
    OTHER = 'other'

    LOCATION_CHOICES = [
            (GROUND_PLANE,_('Ground Plane')),
            (ABOVE_GROUND,_('Above Ground')),
            (OTHER,_('Other')),
            ]

    Location = models.CharField(
            max_length=50,
            help_text=_('Location of Squirrel'),
            choices=LOCATION_CHOICES,
            default=OTHER,
            blank=True,
            )    

    Specific_Location = models.TextField(
            blank=True,
            )

   

    Running = models.BooleanField(
            help_text=_('Wheter or not squirrel was running'),
            default=False,
            )

    Chasing = models.BooleanField(
            help_text=_('Wheter or not squirrel was chasing'),
            default=False,
            )

    Climbing = models.BooleanField(
            help_text=_('Wheter or not squirrel was climbing'),
            default=False,
            )

    Eating = models.BooleanField(
            help_text=_('Wheter or not squirrel was eating'),
            default=False,
            )
   
    Foraging = models.BooleanField(
            help_text=_('Wheter or not squirrel was foraging'),
            default=False,
            )

    Other_Activities = models.TextField(
            blank=True,
            )
            

    Kuks = models.BooleanField(
            help_text=_('Wheter or not squirrel was kuking'),
            default=False,
            )

    Quaas = models.BooleanField(
            help_text=_('Wheter or not squirrel was quaasig'),
            default=False,
            )

    Moans = models.BooleanField(
            help_text=_('Wheter or not squirrel was moaning'),
            default=False,
            )

    Tail_flags  = models.BooleanField(
            help_text=_('Wheter or not squirrel was flagging tail'),
            default=False,
            )

    Tail_twithes = models.BooleanField(
            help_text=_('Wheter or not squirrel was twitching tail'),
            default=False,
            )

    Approaches = models.BooleanField(
            help_text=_('Wheter or not squirrel was approaching'),
            default=False,
            )

    Indifferent = models.BooleanField(
            help_text=_('Wheter or not squirrel was indifferent'),
            default=False,
            )

    Runs_from = models.BooleanField(
            help_text=_('Wheter or not squirrel runs from observer'),
            default=False,
            )
    

