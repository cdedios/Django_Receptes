from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class ReceptaSerializer(HyperlinkedModelSerializer):
	#url = HyperlinkedIdentityField(view_name='recepta-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Recepta
		fields = ('nom', 'description', 'category', 'pais', 'user', 'date')

class PasSerializer(HyperlinkedModelSerializer):
#	url = HyperlinkedIdentityField(view_name='pas-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Pas
		fields = ('text', 'recepta', 'order', 'user', 'date')

class CategoriaSerializer(HyperlinkedModelSerializer):
#	url = HyperlinkedIdentityField(view_name='estil-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Categoria
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date')

class IngredientSerializer(HyperlinkedModelSerializer):
#	url = HyperlinkedIdentityField(view_name='estil-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Ingredient
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date')

class AlimentSerializer(HyperlinkedModelSerializer):
#	url = HyperlinkedIdentityField(view_name='estil-detail')
  	user = CharField(read_only=True)

	class Meta:
		model = Aliment
		fields = ('nom_aliment', 'group', 'ingredients', 'user', 'date')

class MetodeSerializer(HyperlinkedModelSerializer):
#	url = HyperlinkedIdentityField(view_name='estil-detail')
	user = CharField(read_only=True)

	class Meta:
		model = MetodePreparacio
		fields = ('nom', 'ingredients', 'user', 'date')
