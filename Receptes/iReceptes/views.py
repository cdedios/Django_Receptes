from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from iReceptes.models import *
from django.shortcuts import render_to_response

def mainpage(request):
  template = get_template('mainpage.html')
  variables = Context({
      'titlehead': 'Receptes de laguela',
      'pagetitle': 'Welcome to the Receptes  app',
      'user': request.user
    })
  output = template.render(variables)
  return HttpResponse(output)

#RECEPTA
def receptes_list(request):
  variables = Context({
      'titlehead': 'Llista de totes les Receptes',
      'pagetitle': 'Receptes  app',
      'Receptas' : Recepta.objects.all      
    })
  context = RequestContext(request)
  return render_to_response('receptes.html',variables,context)

def recepta_desc(request, id):
  try:
    recepta = Recepta.objects.get(pk=id)
    passos = Pas.objects.filter(recepta=recepta).order_by('order')
    ingredients = Ingredient.objects.filter(recepta=recepta)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'nom_recepta' : recepta.nom ,
        'descripcio_recepta' : recepta.description,
        'categoria_recepta' : recepta.category,
        'Passos' : passos ,
			  'Ingredients' : ingredients ,
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('recepta.html',param,context)

#INGREDIENTS
def ingredients_list(request):
  variables = Context({
      'titlehead': 'Llista de tots els Ingredients',
      'pagetitle': 'Receptes  app',
      'Ingredients' : Ingredient.objects.all      
    })
  context = RequestContext(request)
  return render_to_response('ingredients.html',variables,context)

def ingredient_desc(request, id):
  try:
    ingredient = Ingredient.objects.get(pk=id)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
        'ingredient' : ingredient,
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('ingredient.html',param,context)

#ALIMENTS
def aliments_list(request):
  variables = Context({
      'titlehead': 'Llista de tots els Aliments',
      'pagetitle': 'Receptes  app',
      'Aliments' : Aliment.objects.all      
    })
  context = RequestContext(request)
  return render_to_response('aliments.html',variables,context)

def aliment_desc(request, id):
  try:
    aliment = Aliment.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(aliment=aliment)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'aliment_nom' : aliment.nom ,
        'Ingredients' : ingredients,
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('aliment.html',param,context)

#CATEGORIA
def categories_list(request):
  variables = Context({
      'titlehead': 'Llista de totes les Categories',
      'pagetitle': 'Receptes  app',
      'Categories' : Categoria.objects.all      
    })
  context = RequestContext(request)
  return render_to_response('categories.html',variables,context)

def categoria_desc(request, id):
  try:
    categoria = Categoria.objects.get(pk=id)
    receptes = Recepta.objects.filter(category=categoria)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'categoria_nom' : categoria.nom ,
        'Receptes' : receptes,
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('categoria.html',param,context)

#PASSOS
def passos_list(request):
  variables = Context({
      'titlehead': 'Llista de tots els Passos',
      'pagetitle': 'Receptes  app',
      'Passos' : Pas.objects.all      
    })
  context = RequestContext(request)
  return render_to_response('passos.html',variables,context)

def pas_desc(request, id):
  try:
    pas = Pas.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(pas=pas)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'pas' : pas ,
			  'Ingredients' : ingredients 
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('pas.html',param,context)

#METODES
def metodes_list(request):
  variables = Context({
      'titlehead': 'Llista de tots els Metodes',
      'pagetitle': 'Receptes  app',
      'Metodes' : MetodePreparacio.objects.all(),      
    })
  context = RequestContext(request)
  return render_to_response('metodes.html',variables,context)

def metode_desc(request, id):
  try:
    metode = MetodePreparacio.objects.get(pk=id)
    ingredients = Ingredient.objects.filter(prep_method = metode)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'metode_nom' : metode.nom ,
        'Ingredients' : ingredients, 
        }
  except Recepta.DoesNotExist:
    raise Http404
  return render_to_response('metode.html',param,context)
