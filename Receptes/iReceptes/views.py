from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from iReceptes.models import *
from django.shortcuts import render_to_response,get_object_or_404

from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from forms import *
from django.utils.decorators import method_decorator

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import RecepptaSerializer, PasSerializer, IngredientSerializer, CategoriaSerializer, AlimentSerializer, MetodeSerializer

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

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
    recepta = Recepta.objects.get(idRecepta=id)
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

class ReceptaCreate(CreateView):
	model = Recepta
	template_name = 'form.html'
	form_class = ReceptaForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(ReceptaCreate, self).form_valid(form)

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
    ingredient = Ingredient.objects.get(idIngredient=id)
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
    aliment = Aliment.objects.get(idAliment=id)
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
    categoria = Categoria.objects.get(idCategoria=id)
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

class CategoriaCreate(CreateView):
	model = Categoria
	template_name = 'form.html'
	form_class = CategoriaForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(ReceptaCreate, self).form_valid(form)

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
    pas = Pas.objects.get(idPas=id)
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
    metode = MetodePreparacio.objects.get(idMetode=id)
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

#SEGONA PART

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ingredient = Ingredient.objects.get(id=self.kwargs['pk'])
        return super(IngredientCreate, self).form_valid(form)

class IngredientUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm

#API RestFul
class APIReceptaList(generics.ListCreateAPIView):
	model = Recepta
	serializer_class = GratacelSerializer

class APIGratacelDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Gratacel
	serializer_class = GratacelSerializer

class APIEstilList(generics.ListCreateAPIView):
	model = Estil
	serializer_class = EstilSerializer

class APIEstilDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Estil
	serializer_class = EstilSerializer

class APIMaterialList(generics.ListCreateAPIView):
	model = Material
	serializer_class = MaterialSerializer

class APIMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Material
	serializer_class = MaterialSerializer

class APIArquitecteList(generics.ListCreateAPIView):
	model = Arquitecte
	serializer_class = ArquitecteSerializer

class APIArquitecteDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Arquitecte
	serializer_class = ArquitecteSerializer

