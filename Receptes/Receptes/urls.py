from django.conf.urls import patterns, include, url
from django.conf import settings
from iReceptes.views import *

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
#from rest_framework.urlpatterns import format_suffix_patterns

from iReceptes.models import *
from iReceptes.forms import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{ 'next_page' : '/'}),
    url(r'^login/$','django.contrib.auth.views.login'),

#RECEPTES
    # ex: /receptes/
    url(r'^receptes/$', receptes_list),
    # ex: /receptes/1/
    url(r'^receptes/(?P<id>\w+)/$', recepta_desc),
#    url(r'^receptes/create/$', ReceptaCreate.as_view(), name='recepta_create'),
    
#INGREDIENTS
    # ex: /ingredients/
    url(r'^ingredients/$', ingredients_list),
    # ex: /ingredients/1/
    url(r'^ingredients/(?P<id>\w+)/$', ingredient_desc),
    # ex: /receptes/1/ingredients/1
    url(r'^receptes/(?P<pkr>\d+)/ingredients/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Ingredient,
            template_name='ingredient.html'),
        name='ingredient_detail'),
##AQUI MADAFAKAAAAAA
# EL QUERYSET NO ES .ALL ES FILTER PERO NO SE COM ES PASSA EL PARAMETRE PK 

    # ex: /receptes/1/ingredients/
    url(r'^receptes/(?P<pk>\d+)/ingredients/$',
        ListView.as_view(
            queryset=Ingredient.objects.all,
            context_object_name='Ingredients',
            template_name='ingredients.html'),
        name='ingredients_list'),

    # ex: /receptes/1/ingredients/1/edit/
    url(r'^receptes/(?P<pkr>\d+)/ingredients/(?P<pk>\d+)/edit/$',
        IngredientUpdate.as_view(),
        name='dish_edit'),

    # ex: /receptes/1/ingredients/create
    url(r'^receptes/(?P<pk>\d+)/ingredients/create/$',
        IngredientCreate.as_view(),
        name='ingredient_create'),

    #ALIMENTS
    url(r'^aliments/$', aliments_list),
    url(r'^aliments/(?P<id>\w+)/$', aliment_desc),
    url(r'^aliments/(?P<id>\w+)/$', aliment_desc),

    #CATEGORIES
    url(r'^categories/$', categories_list),
    url(r'^categories/(?P<id>\w+)/$', categoria_desc),
    
    #PASSOS
    url(r'^passos/$', passos_list),
    url(r'^passos/(?P<id>\w+)/$', pas_desc),
    #url(r'^receptes/(?P<id>\w+)/passos/$',
    #    ListView.as_view(
    #        queryset=Pas.objects.filter(pk=id),
    #        context_object_name='passos',
    #        template_name='iReceptes/passos_list.html'),
    #    name='passos_list'),

    #METODES PREPARACIO
    url(r'^metodes/$', metodes_list),
    url(r'^metodes/(?P<id>\w+)/$', metode_desc),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
)
