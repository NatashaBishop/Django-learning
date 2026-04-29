Geting the record I want to update:

    >>> from members.models import Member
    >>> x = Member.objects.all()[4]  # index 4 is "Stale Refsnes"
See what it is: 

    >>> x.firstname    
output: 

    'Stale' 
Change the record: 

    >>> x.firstname = "Stalikken"
    >>> x.save() 
Check member table:

    >>> Member.objects.all().values() 
Output:

    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
    {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
    {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
    {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
    {'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'},
    {'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>
