
from django.shortcuts import render
from django.db.models import Q
from .models import Country, Issue
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from string import ascii_uppercase
from random import choice

def index(request):
    print("Hello")
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
    context = {'countries': Country.objects.all()} 
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        term = data['term']
        print(term)
        matching_countries = Country.objects.filter(Q(name__icontains=term))# | Q(issues__icontains=term)) 
        # context = {'countries': matching_countries}
        print(matching_countries)
        return JsonResponse({'message': 'hi'})

    return render(request, 'countrys/index.html', context)
    