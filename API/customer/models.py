from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Customer(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50,default='')
    location=models.CharField(max_length=50,default='')
    starting_time=models.IntegerField(default=666)
    ending_time=models.IntegerField(default=666)

    def __str__(self):
        return self.username

#super_user=kislay
#password=kislay

class Service(models.Model):
    username=models.CharField(max_length=50)
    date=models.CharField(max_length=50,default='')
    timeslot=models.CharField(max_length=50,default='')
    worktime=models.IntegerField(default=666)
    required=models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Employee(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    working=models.IntegerField(default=1)
    date=models.CharField(max_length=50,default='')
    timeslot=models.CharField(max_length=50,default='')
    a=10
    def __str__(self):
        return self.username


