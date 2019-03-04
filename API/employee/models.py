from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.name

