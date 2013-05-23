from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class ReceptaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='recepta-detail')
	category = HyperlinkedRelatedField(many=False, read_only=True, view_name='categoria-detail')	
	user = CharField(read_only=True)

	class Meta:
		model = Recepta
		fields = ('nom', 'description','category', 'user', 'date')

class PasSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='material-detail')
	recepta = HyperlinkedRelatedField(many=True, read_only=True, view_name='recepta-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Pas
		fields = ('text', 'recepta', 'order', 'user', 'date')

class CategoriaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='estil-detail')
	gratacel_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='xxx-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Estil
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date')

