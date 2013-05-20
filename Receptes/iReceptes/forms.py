from django.forms import ModelForm
from iReceptes.models import *

class ReceptaForm(ModelForm):
  class Meta:
    model = Recepta

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient

class AlimentForm(ModelForm):
  class Meta:
    model = Aliment

class CategoriaForm(ModelForm):
  class Meta:
    model = Categoria

class PasForm(ModelForm):
  class Meta:
    model = Pas

class MetodePreparacioForm(ModelForm):
  class Meta:
    model = MetodePreparacio
