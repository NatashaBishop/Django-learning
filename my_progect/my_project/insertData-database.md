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

     <QuerySet []> # QuerySet is a collection of data from a database
check member table:

    >>> Member.objects.all().values()


# Add a record to table from command line:

    >>> member = Member(firstname='Emil', lastname='Refsnes')
    >>> member.save() 
# See Member table:

    >>> Member.objects.all().values()
# Output:

    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]> 
# write multiple records to table:  
I design  a list of Member objects, then execute .save() on each entry (loop):

    >>> member1 = Member(firstname='Tobias', lastname='Refsnes')
    >>> member2 = Member(firstname='Linus', lastname='Refsnes')
    >>> member3 = Member(firstname='Lene', lastname='Refsnes')
    >>> member4 = Member(firstname='Stale', lastname='Refsnes')
    >>> member5 = Member(firstname='Jane', lastname='Doe')
    >>> members_list = [member1, member2, member3, member4, member5]
    >>> for x in members_list:
    ...   x.save()
    ...
    >>> 
    # to exit the for loop hit "enter" one more time at the end
Output:checking on the members input

    >>> Member.objects.all().values() 
