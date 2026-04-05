#creating table (object or model) 2 store customer data:
from django.db import models

class Customers(models.Model):
firstNameCustomer = models.CharField(max_length=255)
lastNameCustomer = models.CharField(max_length=255)
