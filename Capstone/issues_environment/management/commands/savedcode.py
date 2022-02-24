from django.core.management.base import BaseCommand
import json

from numpy import array
from issues_environment.models import Country, Issue
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        continents = os.listdir('data')
        
        no_name_list = []
        for continent in continents: # continent
            entries = os.listdir(f'data\{continent}')
            for entry in entries: #countries
                try:
                    with open(f'data/{continent}/{entry}', 'r', encoding='utf-8') as f:
                        country_data = (json.load(f))
                        country_name = (country_data['Government']['Country name']['conventional short form']['text'] )
                        print('Country Name: ', country_name)
                        if country_name == "none":
                            #add entry to list
                            no_name_list.append(entry)
                except KeyError:
                    print('sorry no data available')
        print(no_name_list)
                   