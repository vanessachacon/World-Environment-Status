from django.db import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
 return HttpResponse('hello')


