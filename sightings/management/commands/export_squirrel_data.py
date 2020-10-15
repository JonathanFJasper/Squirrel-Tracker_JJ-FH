from django.core.management.base import BaseCommand, CommandError
import csv 
from sightings.models import Squirrel 
import sys 

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path',type=str,help="csv file")

    def handle(self, path, **options):
        with open(path, 'w', newline='') as field1:
            model = Squirrel
            field_names = [field2.name for field2 in model._meta.fields]
            writer  = csv.writer(field1, quoting=csv.QUOTE_ALL)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, field3) for field3 in field_names])

        self.stdout.write(self.style.SUCCESS('Successfully exported!')) 
