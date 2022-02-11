
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Countries, Issues



class Command(BaseCommand):
    def handle(self,*args,**options):
        # factbook_path = '../../factbook.json/'
        # for country in countries:
        us_data_filepath = 'data/north-america/us.json'
        with open(us_data_filepath, 'r', encoding='utf-8') as f:
            us_data = json.load(f)   
        e_data=(us_data['Environment']['Environment - current issues']['text'])
        env_data = (e_data.split('; '))
        # print(env_data)
        for issue in env_data:
            print(issue)

