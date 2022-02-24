
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        entries = os.listdir('data/north-america')
        for entry in entries:
            
            with open(f'data/north-america/{entry}', 'r', encoding='utf-8') as f:
                country_data = (json.load(f))
            country_name = (country_data['Government']['Country name'] ['conventional short form']['text'])
            print('Country Name: ', country_name)
            country, _created = Country.objects.get_or_create(name=country_name)

            e_data = (country_data['Environment']['Environment - current issues']['text'])
            env_data = (e_data.split('; '))
            for issue_text in env_data:
                issue, _created = Issue.objects.get_or_create(text=issue_text)
                print(issue)
                country.issues.add(issue)
            country.save()
            

 