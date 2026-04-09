#creating table (object or model) 2 store customer data:
from django.db import models

class Customers(models.Model):
firstNameCustomer = models.CharField(max_length=255) #CharField=text field
lastNameCustomer = models.CharField(max_length=255)
#run this command: python manage.py makemigrations members
#with output:
'''Migrations for 'members':
  members\migrations\0001_initial.py
    - Create model Member

(myworld) C:\Users\Your Name\myworld\my_tennis_club> '''

