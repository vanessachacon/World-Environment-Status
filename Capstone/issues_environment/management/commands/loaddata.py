from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue

class Command(BaseCommand):
    def handle(self,*args,**options):
        print('command ran')