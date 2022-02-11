
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Countries, Issues



class Command(BaseCommand):
    def handle(self,*args,**options):
        factbook_path = '../../factbook.json/'
        # for country in countries:
        us_data_filepath = factbook_path + 'north-america/us.json'
        with open(us_data_filepath, 'r', encoding='utf-8') as f:
            us_data = json.load(f)   
        e_data=(us_data['Environment']['Environment - current issues']['text'])
        env_data = (e_data.split('; '))
        # print(env_data)
        for issue in env_data:
            print(issue)

# for issue in data.split('; '):
#     issue = issue(text)
#     print(type(issue))
#     print()

# class Country:
#     def_init_(self,name, issues):
#     self.name = name
#     self.issues = data.split(';')
# need to import json somewhere (views?)
# data= json.loads() ---- ??? environmental issues or whatever the name of it is in json right?
# print(data)
# with open ('country.json') as f:
    # data = json.load(f) (name guessed at this point)
# custom management
#
