from django.core.management.base import BaseCommand
import json

from numpy import array
from issues_environment.models import Country, Issue
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        continents = os.listdir('data')
        
        no_name_list = []
        no_env_list = []
        for continent in continents: # continent
            entries = os.listdir(f'data\{continent}')
            for entry in entries: #countries
                try:
                    with open(f'data/{continent}/{entry}', 'r', encoding='utf-8') as f:
                        country_data = (json.load(f))
                    country_name = (country_data['Government']['Country name']['conventional short form']['text'] )
                    print(country_name)
                    if country_name == "none":
                        no_name_list.append(entry)
                except KeyError:
                    print('sorry no data available')
                country,_created = Country.objects.get_or_create(name=country_name)

                try:
                    e_data = (country_data['Environment']['Environment - current issues']['text'])
                    env_data = (e_data.split('; '))
                    print(env_data)
                    if e_data == "none":
                        no_env_list.append(entry)
                except KeyError:
                    print('sorry no data available')
                for issue_text in env_data:
                    issue, _created = Issue.objects.get_or_create(text=issue_text)
                    print(issue)
                    country.issues.add(issue)
                    country.save()
                
        print(no_name_list)
        print(no_env_list)