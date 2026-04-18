The Members table created in 0001_initial.py (and only after I run: python manage.py migrate) is empty.  
I will use the Python interpreter (Python shell) to add some members to it.  
To open a Python shell, I type command: 

    python manage.py shell  
Now I am in the shell, the result will look like this:@ 

    Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb 4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>>
after that >>> I run the following:

    >>> from members.models import Member 

ckick enter and see empty Member table:

    >>> Member.objects.all() 
    
This gives me empty QuerySet object:

     <QuerySet []>

