from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    issues = models.ManyToManyField('Issue')

    def __str__(self):
        return self.name



class Issue (models.Model):
    issue = models.CharField(max_length=50)

    def __str__(self):
        return self.issue

# for issue in data.split('; '):
#     issue = issue(text)
#     print(type(issue))
#     print()

# class Country:
#     def_init_(self,name, issues):
#     self.name = name
#     self.issues = data.split(';')
# need to import json somewhere (views?)
# data= json.loads() ---- ??? environmental issues or whatever the name of it is in json right?
# print(data)

# with open ('country.json') as f:
    # data = json.load(f) (name guessed at this point)


# custom management
#
