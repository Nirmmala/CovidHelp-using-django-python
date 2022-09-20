from enum import auto
from tkinter import CASCADE
from turtle import ondrag
# from typing_extensions import self
from django.db import models

# Create your models here.

# =======state======================
class State(models.Model):  
    name = models.CharField(max_length=50, null =False, blank =False)

    def __str__(self):
        return self.name

# =============city=====================
class City(models.Model):
    name = models.CharField(max_length=50, null =False, blank =False)
    state = models.ForeignKey(State, on_delete = models.CASCADE, related_name= 'cities')

    def __str__(self):
        return self.name


# =============hospital=====================

class Hospital(models.Model):
    name = models.CharField(max_length=50, null =False, blank =False)
    phone = models.CharField(max_length=10, null =False, blank =False)
    address = models.CharField(max_length=200, null =False, blank =False)
    city = models.ForeignKey(City, on_delete = models.CASCADE, related_name= 'hospital')

    def __str__(self):
        return self.name

# =============service=====================

class Facility(models.Model):

   title = models.CharField(max_length=60, null= False, blank=False, default="")

   def __str__(self):
     return self.title


class Availability(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name='availabilities')

    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, related_name='availabilities')

    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)


   

    def __str__(self):
       return f'{self.hospital.name} - {self.facility.title}'




