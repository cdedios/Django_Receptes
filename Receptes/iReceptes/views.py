from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def mainpage(request):
  template = get_template('mainpage.html')
  variables = Context({
    'titlehead': 'Receptes de laguela',
    'pagetitle': 'Welcome to the Receptes  app',
    'contentbody': 'Managing non legal funding since 2013'
  })
  output = template.render(variables)
  return HttpResponse(output)
