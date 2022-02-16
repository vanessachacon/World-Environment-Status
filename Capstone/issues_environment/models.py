from django.db import models


class Country(models.Model):
    class Meta: 
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=50)
    issues = models.ManyToManyField('Issue')

    def __str__(self):
        return self.name



class Issue(models.Model):
    text = models.CharField(max_length=50)


    def __str__(self):
        return self.text

