from django.contrib import admin
from iReceptes.models import Ingredient
from iReceptes.models import Categoria
from iReceptes.models import Recepta
from iReceptes.models import GrupAlimentari
from iReceptes.models import Aliment
from iReceptes.models import Unitat
from iReceptes.models import Pas
from iReceptes.models import MetodePreparacio

admin.site.register(Ingredient)
admin.site.register(Categoria)
admin.site.register(Recepta)
admin.site.register(GrupAlimentari)
admin.site.register(Aliment)
admin.site.register(Unitat)
admin.site.register(Pas)
admin.site.register(MetodePreparacio)
