views.py contains functions that take http requests and return http response.  
views.py file is where we gather the information we need to send back a proper response  
usual location: 

    my_project/bartermonster/views.py
Example of views.py:
    
    from django.shortcuts import render
    from django.http import HttpResponse
    
    def members(request):
        return HttpResponse("Hello world!")
