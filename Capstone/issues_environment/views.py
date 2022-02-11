
from .models import Countries, Issues

from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')





#  do I do data.split in views +function

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
