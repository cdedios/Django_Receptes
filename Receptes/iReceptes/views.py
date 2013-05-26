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
from django.views.generic import DetailView, UpdateView, DeleteView
from forms import *
from django.utils.decorators import method_decorator

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import ReceptaSerializer, PasSerializer, IngredientSerializer, CategoriaSerializer, AlimentSerializer, MetodeSerializer

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
    recepta = Recepta.objects.get(pk=id)
    passos = Pas.objects.filter(recepta=recepta).order_by('order')
    ingredients = Ingredient.objects.filter(recepta=recepta)
    context = RequestContext(request)
    param = {
        'titlehead' : "Detalls recepta",
			  'nom_recepta' : recepta.nom ,
        'descripcio_recepta' : recepta.description,
        'categoria_recepta' : recepta.category,
        'pais' : recepta.pais,
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
			  'aliment_nom' : aliment.nom_aliment ,
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

#SEGONA PART

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IngredientCreate, self).form_valid(form)

class PasCreate(LoginRequiredMixin, CreateView):
    model = Pas
    template_name = 'form.html'
    form_class = PasForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PasCreate, self).form_valid(form)

class AlimentCreate(LoginRequiredMixin, CreateView):
    model = Aliment
    template_name = 'form.html'
    form_class = AlimentForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(AlimentCreate, self).form_valid(form)

class MetodeCreate(LoginRequiredMixin, CreateView):
    model = MetodePreparacio
    template_name = 'form.html'
    form_class = MetodePreparacioForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MetodeCreate, self).form_valid(form)

class ReceptaCreate(CreateView):
	model = Recepta
	template_name = 'form.html'
	form_class = ReceptaForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(ReceptaCreate, self).form_valid(form)

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'form.html'
    form_class = CategoriaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CategoriaCreate, self).form_valid(form)

class IngredientUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Ingredient
    template_name = 'form.html'
    form_class = IngredientForm

class PasUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Pas
    template_name = 'form.html'
    form_class = PasForm

class CategoriaUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Categoria
    template_name = 'form.html'
    form_class = CategoriaForm

class ReceptaUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Recepta
    template_name = 'form.html'
    form_class = ReceptaForm

class AlimentUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Aliment
    template_name = 'form.html'
    form_class = AlimentForm

class MetodeUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = MetodePreparacio
    template_name = 'form.html'
    form_class = MetodePreparacioForm

#API RestFul
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIReceptaList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Recepta
  serializer_class = ReceptaSerializer

class APIReceptaDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Recepta
  serializer_class = ReceptaSerializer

class APIIngredientList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Ingredient
  serializer_class = IngredientSerializer

class APIIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Ingredient
  serializer_class = IngredientSerializer

class APIPasList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Pas
  serializer_class = PasSerializer

class APIPasDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Pas
  serializer_class = PasSerializer

class APICategoriaList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Categoria
  serializer_class = CategoriaSerializer

class APICategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Categoria
  serializer_class = CategoriaSerializer

class APIAlimentList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Aliment
  serializer_class = AlimentSerializer

class APIAlimentDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = Aliment
  serializer_class = AlimentSerializer

class APIMetodeList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = MetodePreparacio #CUIDADO AQUI
  serializer_class = MetodeSerializer

class APIMetodeDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  model = MetodePreparacio #CUIDADO AQUI
  serializer_class = MetodeSerializer

