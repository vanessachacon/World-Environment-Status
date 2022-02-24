
from django.shortcuts import render
from django.db.models import Q
from .models import Country, Issue
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from string import ascii_uppercase
from random import choice

def index(request):

    return render(request,'issues-environment/index.html')

# def get_info(request):
#     countries = []
#     for country in Country.objects.all():
#         print(country)
#         country_dict = {'name': country.name, 'issues': []}
#         for issue in country.issues.all():
#             print(issue)
#             country_dict['issues'].append(issue.text)
#         countries.append(country_dict)

#     nonsense = ''
#     for _ in range(10):
#         nonsense += choice(ascii_uppercase)
#     return JsonResponse({
#         'message': 'the json response worked',
#         'nonsense': nonsense,
#         'countries': countries
#     })



def country_issue_info(request):
    if request.method == 'POST':
        search = json.loads(request.body)
        text = search.get('searchEntry')
        context = {'countries': Country.objects.all()} 
        term = search['searchEntry']
        matching_countries = Country.objects.filter(Q(name__icontains=term)) #| Q(issues__icontains=term)
        context = {'countries': matching_countries} # {% for country in matching_countries %}
        # print(matching_countries)
        countries = []
        for country in matching_countries:
            country_dict = {'name': country.name, 'issues': []}
            countries.append(country_dict)
            print(country.name)
            print(country.issues.all())
            for issue in country.issues.all():
                print(issue.text)
                country_dict['issues'].append(issue.text)
            print()
        # print(context)

        data = {'countries': countries}
        
        
    return JsonResponse (data)
    