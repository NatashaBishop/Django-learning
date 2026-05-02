Getting record I want to delete:

    >>> from members.models import Member
    >>> x = Member.objects.all()[5] 
Read member at index 5 ("John Smith"):

    >>> x.firstname

it reads out :

    John
    
