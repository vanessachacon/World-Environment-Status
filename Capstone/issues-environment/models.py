from django.db import render, models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

class Countries(models.Model):
    name = models.CharField(max_length=50)
    issuesType = models.ManyToManyField('Issue')

class Issue (models.Model):
    issue = models.CharField (max_length=50)
