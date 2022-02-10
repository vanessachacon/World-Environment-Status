import json
from .models import Country, Issue

from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')


# question on text, json, custom management example