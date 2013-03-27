from django.contrib import admin
from iReceptes.models import Ingredient
from iReceptes.models import Cuiner
from iReceptes.models import Recepta

admin.site.register(Ingredient)
admin.site.register(Cuiner)
admin.site.register(Recepta)
