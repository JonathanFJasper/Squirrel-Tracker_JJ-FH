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
                    unique_squirrel_id = i[2],
                    shift = i[4],
                    date = i[5][4:8]+'-'+ i[5][0:2]+'-'+ i[5][2:4],
                    age = i[7],
                    primary_fur_color = i[8],
                    location = i[12],
                    specific_location = i[14],
                    running = True if i[15].lower()=='true' else False,
                    chasing = True if i[16].lower()=='true' else False,
                    climbing = True if i[17].lower()=='true' else False,
                    eating = True if i[18].lower()=='true' else False,
                    foraging = True if i[19].lower()=='true' else False,
                    other_activities = i[20],
                    kuks = True if i[21].lower()=='true' else False,
                    quaas = True if i[22].lower()=='true' else False,
                    moans = True if i[23].lower()=='true' else False,
                    tail_flags = True if i[24].lower()=='true' else False,
                    tail_twitches = True if i[25].lower()=='true' else False,
                    approaches = True if i[26].lower()=='true' else False,
                    indifferent = True if i[27].lower()=='true' else False,
                    runs_from = True if i[28].lower()=='true' else False,)
            

                    


