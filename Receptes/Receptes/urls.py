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
    url(r'^admin/', include(admin.site.urls)),


#CREACIO

    # ex: /ingredients/create/
    url(r'^ingredients/create/$', IngredientCreate.as_view(), name='ingredient_create'),  
    # ex: /receptes/1/ingredients/create
    url(r'^receptes/(?P<pk>\d+)/ingredients/create/$',
        IngredientCreate.as_view(),
        name='ingredient_create'),
    # ex: /passos/create/
    url(r'^passos/create/$', PasCreate.as_view(), name='pas_create'),  
    # ex: /receptes/1/passos/create
    url(r'^receptes/(?P<pk>\d+)/passos/create/$',
        PassosCreate.as_view(),
        name='pas_create'),




    # ex: /receptes/1/ingredients/1
    #url(r'^receptes/(?P<pkr>\d+)/ingredients/(?P<pk>\d+)/$',
    #    DetailView.as_view(
    #        model=Ingredient,
    #        template_name='ingredient.html'),
    #    name='ingredient_detail'),

##AQUI MADAFAKAAAAAA
# EL QUERYSET NO ES .ALL ES FILTER PERO NO SE COM ES PASSA EL PARAMETRE PK 

    # ex: /receptes/1/ingredients/
    #url(r'^receptes/(?P<pk>\d+)/ingredients/$',
    #    ListView.as_view(
    #        queryset=Ingredient.objects.all,
    #        context_object_name='Ingredients',
    #        template_name='ingredients.html'),
    #    name='ingredients_list'),
 
    # ex: /receptes/1/ingredients/1/edit/
    url(r'^receptes/(?P<pkr>\d+)/ingredients/(?P<pk>\d+)/edit/$',
        IngredientUpdate.as_view(),
        name='dish_edit'),
    # ex: /ingredients/1/edit/
    url(r'^/ingredients/(?P<pk>\d+)/edit/$',
        IngredientUpdate.as_view(),
        name='dish_edit'),

    #ALIMENTS
    #url(r'^aliments/$', aliments_list),
    #url(r'^aliments/(?P<id>\w+)/$', aliment_desc),

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
)



#RESTful API
urlpatterns += patterns('',
    url(r'^api/receptes/$', APIReceptaList.as_view(), name='receptes-list'),
    url(r'^api/receptes/(?P<pk>\d+)/$', APIReceptaDetail.as_view(), name='recepta-detail'),

    url(r'^api/passos/$', APIPasList.as_view(), name='passos-list'),
    url(r'^api/passos/(?P<pk>\d+)/$', APIPasDetail.as_view(), name='pas-detail'),

    url(r'^api/ingredients/$', APIIngredientList.as_view(), name='ingredients-list'),
    url(r'^api/ingredients/(?P<pk>\d+)/$', APIIngredientDetail.as_view(), name='ingredient-detail'),

    url(r'^api/aliments/$', APIAlimentList.as_view(), name='aliments-list'),
    url(r'^api/aliments/(?P<pk>\d+)/$', APIAlimentDetail.as_view(), name='aliment-detail'),

    url(r'^api/categories/$', APICategoriaList.as_view(), name='categories-list'),
    url(r'^api/categories/(?P<pk>\d+)/$', APICategoriaDetail.as_view(), name='categoria-detail'),

    url(r'^api/metodes/$', APIMetodeList.as_view(), name='metodes-list'),
    url(r'^api/metodes/(?P<pk>\d+)/$', APIMetodeDetail.as_view(), name='metode-detail'),
)    

