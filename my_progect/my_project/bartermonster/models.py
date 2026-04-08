#creating table (object or model) 2 store customer data:
from django.db import models

class Customers(models.Model):
firstNameCustomer = models.CharField(max_length=255) #CharField=text field
lastNameCustomer = models.CharField(max_length=255)
#run this command: python manage.py makemigrations members
