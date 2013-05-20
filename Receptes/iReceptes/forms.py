from django.forms import ModelForm
from iReceptes.models import *

class ReceptaForm(ModelForm):
  class Meta:
    model = Recepta
    exclude = ('user',)

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    exclude = ('user',)
