
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue








class Command(BaseCommand):
    def handle(self,*args,**options):
        # factbook_path = '../../factbook.json/'
        # for country in countries:
        us_data_filepath = 'data/north-america/us.json'
        with open(us_data_filepath, 'r', encoding='utf-8') as f:
            us_data = json.load(f)   
        country_names=(us_data['Government']['Country name']['conventional short form']['text'])
        for country_name in country_names:
            country, _created = Country.objects.get_or_create(name = country_names)
            print(country)
        # print(env_data)
        # create the country object
        # get the name out of the data
     
            # country.issues.add(issue) pseudocode


# class Command(BaseCommand):
#     def handle(self,*args,**options):
#         factbook_path = 'career/factbook.json'
#         with open(factbook_path, 'r', encoding='utf-8') as f:
#             all_data = json.load(f)   
#         # for country in countries:
#         # all_data_filepath = 'data/north-america/sb.json'
#         # with open(all_data_filepath, 'r', encoding='utf-8') as f:
#         #     all_data = json.load(f)   
#         print( all_data)
    
#         # create the country object
#         # get the name out of the data
        
#             # country.issues.add(issue) pseudocode

# 
# {'Country name': {'conventional long form': {'text': 'Territorial Collectivity of Saint Pierre and Miquelon'}, 'conventional short form': {'text': 'Saint Pierre and Miquelon'}, 'local long form': {'text': 'Departement de Saint-Pierre et Miquelon'}, 'local short form': {'text': 'Saint-Pierre et Miquelon'}, 'etymology': {'text': 'Saint-Pierre is named after Saint PETER, the patron saint of fishermen; Miquelon may be a corruption of the Basque name Mikelon'}}, '

# OR by ISO code?