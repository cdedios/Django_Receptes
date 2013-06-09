from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class ReceptaSerializer(HyperlinkedModelSerializer):
  user = CharField(read_only=True)
  receptareview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='receptareview-detail')
  class Meta:
    model = Recepta
    fields = ('nom', 'description', 'category', 'pais', 'user', 'date','receptareview_set')

class PasSerializer(HyperlinkedModelSerializer):
	user = CharField(read_only=True)

	class Meta:
		model = Pas
		fields = ('text', 'recepta', 'order', 'user', 'date')

class CategoriaSerializer(HyperlinkedModelSerializer):
	user = CharField(read_only=True)

	class Meta:
		model = Categoria
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date')

class IngredientSerializer(HyperlinkedModelSerializer):
	user = CharField(read_only=True)

	class Meta:
		model = Ingredient
		fields = ('nom', 'dataInici', 'dataFi','calories','carbohydrateContent', 'user', 'date')

class AlimentSerializer(HyperlinkedModelSerializer):
  	user = CharField(read_only=True)

	class Meta:
		model = Aliment
		fields = ('nom_aliment', 'group', 'ingredients', 'user', 'date')

class MetodeSerializer(HyperlinkedModelSerializer):
	user = CharField(read_only=True)

	class Meta:
		model = MetodePreparacio
		fields = ('nom', 'ingredients', 'user', 'date')
