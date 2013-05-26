from django.forms import ModelForm
from iReceptes.models import *

class ReceptaForm(ModelForm):
  class Meta:
    model = Recepta
    exclude = ('user', 'date',)

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    exclude = ('user', 'date',)

class AlimentForm(ModelForm):
  class Meta:
    model = Aliment
    exclude = ('user', 'date',)

class CategoriaForm(ModelForm):
  class Meta:
    model = Categoria
    exclude = ('user', 'date',)

class PasForm(ModelForm):
  class Meta:
    model = Pas
    exclude = ('user', 'date',)

class MetodePreparacioForm(ModelForm):
  class Meta:
    model = MetodePreparacio
    exclude = ('user', 'date',)
