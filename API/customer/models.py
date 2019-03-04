from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    starting_time=models.IntegerField(default=666)
    ending_time=models.IntegerField(default=666)

    def __str__(self):
        return self.name

#super_user=kislay
#password=123456

