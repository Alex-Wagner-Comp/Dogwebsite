from django.db import models
from django.forms import ModelForm

class Dog(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null = True)
    dogname = models.CharField(max_length=200, null = True)
    dogbreed = models.CharField(max_length=200, null=True)
    doggender = models.CharField(max_length=200, null=True)
    dogsize = models.CharField(max_length=200, null=True)
    doghealth = models.CharField(max_length = 200, null=True)
    doghealthphone = models.CharField(max_length=200, null=True)


class Appointment(models.Model):
    dogapptname = models.CharField(max_length=200, null = True)
    lastnameappt = models.CharField(max_length=200, null = True)
    typeofcut = models.CharField(max_length=200, null = True)
    timetakestocut = models.CharField(max_length=200, null = True)
    costofcut = models.CharField(max_length=200, null = True)