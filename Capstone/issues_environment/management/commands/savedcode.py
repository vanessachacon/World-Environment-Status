
import pandas as pd
from django.core.management.base import BaseCommand
import json
from issues_environment.models import Country, Issue
import os

base_dir = 'data/north-america'

data_list = []
for file in os.listdir(base_dir):

    # If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        json_path = os.path.join(base_dir, file)
        json_data = pd.read_json(json_path, lines=True)
        data_list.append(json_data)
print(data_list)

# country_names=(us_data['Government']['Country name']['conventional short form']['text'])
# country, _created = Country.objects.get_or_create(name = country_names)
# print(country)
# if _created:
#     self.stdout.write(f'{country_names} created')
# country.issues.add()
# country.save()

# us_data_filepath = 'data/north-america/us.json'
# with open(us_data_filepath, 'r', encoding='utf-8') as f:
#     us_data = json.load(f)
# e_data=(us_data['Environment']['Environment - current issues']['text'])
# env_data = (e_data.split('; '))

# for issue_text in env_data:
#     issue, _created = Issue.objects.get_or_create(text = issue_text)
#     print(issue)
#     if _created:
#         self.stdout.write(f'{issue} created')
#     country.issues.add(issue)
