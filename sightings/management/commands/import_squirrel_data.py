from django.core.management.base import BaseCommand, CommandError
import csv 
from sightings.models import Squirrel

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', help="csv file", type=str)

    def handle(self, path, **options):
        with open(path, 'r') as x:
            reader = csv.reader(x)
            next(reader)
            for i in reader:
                _, created = Squirrel.objects.get_or_create(
                    X = i[0],
                    Y= i[1],
                    Unique_Squirrel_ID = i[2],
                    Shift = i[4],
                    Date = i[5][4:8]+'-'+ i[5][0:2]+'-'+ i[5][2:4],
                    Age = i[7],
                    Primary_Fur_Color = i[8],
                    Location = i[12],
                    Specific_Location = i[14],
                    Running = True if i[15].lower()=='true' else False,
                    Chasing = True if i[16].lower()=='true' else False,
                    Climbing = True if i[17].lower()=='true' else False,
                    Eating = True if i[18].lower()=='true' else False,
                    Foraging = True if i[19].lower()=='true' else False,
                    Other_Activities = i[20],
                    Kuks = True if i[21].lower()=='true' else False,
                    Quaas = True if i[22].lower()=='true' else False,
                    Moans = True if i[23].lower()=='true' else False,
                    Tail_flags = True if i[24].lower()=='true' else False,
                    Tail_twitches = True if i[25].lower()=='true' else False,
                    Approaches = True if i[26].lower()=='true' else False,
                    Indifferent = True if i[27].lower()=='true' else False,
                    Runs_from = True if i[28].lower()=='true' else False,)
            

         self.stdout.write(self.style.SUCCESS('Successfully imported!'))           


