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
Chack member table:

    >>> Member.objects.all().values() 
