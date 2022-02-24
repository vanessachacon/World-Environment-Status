
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
        # print(context)

        data = {'countries': countries}
        
        
    return JsonResponse (data)
    

    # for (let i=0; i<countries.length; i++) {
    # console.log(countries[i].name)
    # if (countries[i].issues.length > 0) {
    #     console.log('issues', issues)
    # } else {console.log('no issues, perfect environment in this country')
    #        }
}