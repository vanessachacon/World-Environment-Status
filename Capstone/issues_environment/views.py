
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

        matching_issues = Issue.objects.filter(Q(text__icontains=term))
        issues = []
        for issue in matching_issues:
            issue_dict = {'name': issue.text, 'countries': []}
            issues.append(issue_dict)
            print(issue.text)
            # print(issue.issues.all())
            for country in issue.countries.all():
                print(country.name)
                issue_dict['countries'].append(country.name)
            print()
        

        data = {'countries': countries,
                'issues' : issues
                }
        
        
    return JsonResponse (data)
    