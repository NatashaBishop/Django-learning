Django model is an equivalent of a table in a database  
Models are objects and tables in a database.
To create a model, go 2 the models.py file in the /bartermonster/ folder.  
We create table for storing customer data: 

from django.db import models  

class Customers(models.Model):  
  firstNameCustomer = models.CharField(max_length=255)  
  lastNameCustomer = models.CharField(max_length=255)  

Customers is an object, equivalent to a table in the database
## SQLite Database  

When we created the Django project, an empty SQLite database was created in my_project root folder, filename db.sqlite3.  

By default, all Models created in the Django project will be created as tables in database db.sqlite3.
