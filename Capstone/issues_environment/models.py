from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50)
    issues = models.ManyToManyField('Issues')

    def __str__(self):
        return self.name



class Issues (models.Model):
    issues = models.CharField(max_length=50)

    def __str__(self):
        return self.issues

