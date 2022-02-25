from django.db import models


class Country(models.Model):
    class Meta: 
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=500)
    issues = models.ManyToManyField('Issue', related_name='countries') # related_name= keyword argument overrides the default
    # the default way to get all countries related to an issue would be issue.country_set.all()
    # with related_name='countries', you can just do issue.countries.all()

    def __str__(self):
        return self.name



class Issue(models.Model):
    text = models.CharField(max_length=500)


    def __str__(self):
        return self.text

#add counter
