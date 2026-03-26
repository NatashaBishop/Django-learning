#file location: my_project/bartermonster/views.py:
from django.http import HttpResponse
from django.template import loader

def bartermonster(request):
  template = loader.get_template('htmlTest.html')
  return HttpResponse(template.render())
