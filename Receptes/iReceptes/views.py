from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from iReceptes.models import Recepta, Categoria, Aliment, MetodePreparacio, Recepta, Pas, Ingredient

def mainpage(request):
  template = get_template('mainpage.html')
  variables = Context({
      'titlehead': 'Receptes de laguela',
      'pagetitle': 'Welcome to the Receptes  app',
      'contentbody': 'Managing non legal funding since 2013'
    })
  output = template.render(variables)
  return HttpResponse(output)

def receptes_list(request):
  template = get_template('receptes.html')
  variables = Context({
      'titlehead': 'Llista de totes les Receptes',
      'Receptas' : Recepta.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)

def recepta_desc(request):
  template = get_template('recepta.html')
  variables = Context({
      'titlehead': 'Descripcio de la Recepta: ',
      'Recepta' : Recepta.objects.all      
    })
  output = template.render(variables)
  return HttpResponse(output)

def userpage(request, username):
  try:
    user = User.objects.get(username=username)
  except:
    raise Http404('User not found.')

  ingredients = user.recepta_set.all()
  template = get_template('userpage.html')
  variables = Context({
    'username': username,
    'ingredients': ingredients
    })
  output = template.render(variables)
  return HttpResponse(output)
