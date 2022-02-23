
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue
import pandas as pd
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        entries = os.listdir('data/north-america')
        for entry in entries:
            with open(f'data/north-america/{entry}', 'r', encoding='utf-8') as f:
                all_na_data = (json.load(f))
                country_names = (all_na_data['Government']['Country name'] ['conventional short form']['text'])
                country, _created = Country.objects.get_or_create(name=country_names)
                print(country)
            if _created:
                self.stdout.write(f'{country_names} created')
            country.issues.add()
            country.save()

        for entry in entries:
            with open(f'data/north-america/{entry}', 'r', encoding='utf-8') as f:
                all_na_data = (json.load(f))
            e_data = (all_na_data['Environment']['Environment - current issues']['text'])
            env_data = (e_data.split('; '))
        for issue_text in env_data:
            issue, _created = Issue.objects.get_or_create(text=issue_text)
            print(issue)
            if _created:
                self.stdout.write(f'{issue} created')
            country.issues.add(issue)

#   bd_data = json.load(f)
#             ca_data = json.load(f)
#             gl_data = json.load(f)
#             ip_data = json.load(f)
#             mx_data = json.load(f)
#             sb_data = json.load(f)
