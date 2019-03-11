from django.contrib import admin
from .models import Customer,Service,Employee
# Register your models here.
admin.site.register([Customer,Service,Employee])