
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue



class Command(BaseCommand):
    def handle(self,*args,**options):
        us_data_filepath = 'data/north-america/us.json'
        with open(us_data_filepath, 'r', encoding='utf-8') as f:
            us_data = json.load(f)   
        e_data=(us_data['Environment']['Environment - current issues']['text'])
        env_data = (e_data.split('; '))
        for issue_text in env_data:
            issue, _created = Issue.objects.get_or_create(text = issue_text)
            print(issue)

