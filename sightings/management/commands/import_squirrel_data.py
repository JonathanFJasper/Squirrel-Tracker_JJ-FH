from django.core.management.base import BaseCommand, CommandError
import csv 
import sightings.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='/path/to/file.csv')

    def handle(self, *args, **options):
        path = options['path']
        with open(path, mode='r') as x:
            squirrel_data = csv.reader(x)
                       
            
            squirrel_sightings=[]
            squirrel_id=[]
            
            for i in squirrel_data:
                if i.get('Unique Squirrel ID') in squirrel_id:
                    continue
                else:
                    item = Squirrel(
                    X = i.get('X'),
                    Y = i.get('Y'),
                    Unique_Squirrel_ID = i.get('Unique Squirrel ID'),
                    Shift = i.get('Shift'),
                    Date = datetime.date(int(i.get('Date')[-4:]),int(i.get('Date')[:2]),int(i.get('Date')[2:4])),
                    Age = i.get('Age'),
                    Primary_Fur_Color = i.get('Primary Fur Color'),
                    Location = i.get('Location'),
                    Specific_Location = i.get('Specific Location'),
                    Running = True if i.get('Running').lower()=='true' else False,
                    Chasing = True if i.get('Chasing').lower()=='true' else False,
                    Climbing = True if i.get('Climbing').lower()=='true' else False,
                    Eating = True if i.get('Eating').lower()=='true' else False,
                    Foraging = True if i.get('Foraging').lower()=='true' else False,
                    Other_Activities = i.get('Other Activities'),
                    Kuks = True if i.get('Kuks').lower()=='true' else False,
                    Quaas = True if i.get('Quaas').lower()=='true' else False,
                    Moans = True if i.get('Moans').lower()=='true' else False,
                    Tail_flags = True if i.get('Tail flags').lower()=='true' else False,
                    Tail_twitches = True if i.get('Tail twitches').lower()=='true' else False,
                    Approaches = True if i.get('Approaches').lower()=='true' else False,
                    Indifferent = True if i.get('Indifferent').lower()=='true' else False,
                    Runs_from = True if i.get('Runs from').lower()=='true' else False
                    )
                    squirrel_sightings.append(item)
                    squirrel_id.append(i.get('Unique Squirrel ID'))
            
            Squirrel.objects.bulk_create(squirrel_sightings)
            

                    


