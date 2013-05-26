from django.conf.urls import patterns, include, url
from django.conf import settings
from iReceptes.views import *

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
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

	#RECEPTES
    url(r'^receptes/$', receptes_list),
    url(r'^receptes/(?P<id>\d+)/$', recepta_desc,name="recepta_detail"),
	#ALIMENTS
    url(r'^aliments/$', aliments_list),
    url(r'^aliments/(?P<id>\d+)/$', aliment_desc,name="aliment_detail"),
    #CATEGORIES
    url(r'^categories/$', categories_list),
    url(r'^categories/(?P<id>\d+)/$', categoria_desc,name="categoria_detail"),    
    #PASSOS
    url(r'^passos/$', passos_list),
    url(r'^passos/(?P<id>\d+)/$', pas_desc,name="pas_detail"),
    #METODES PREPARACIO
    url(r'^metodes/$', metodes_list),
    url(r'^metodes/(?P<id>\d+)/$', metode_desc, name="metode_detail"),
	#INGREDIENTS
	url(r'^ingredients/$', ingredients_list),
    url(r'^ingredients/(?P<id>\d+)/$', ingredient_desc, name="ingredient_detail"),


#CREACIO

    # ex: /ingredients/create/
    url(r'^ingredients/create/$', IngredientCreate.as_view(), name='ingredient_create'),  
    # ex: /passos/create/
    url(r'^passos/create/$', PasCreate.as_view(), name='pas_create'), 
    # ex: /categories/create/
    url(r'^categories/create/$', CategoriaCreate.as_view(), name='categria_create'),
    # ex: /receptes/create/
    url(r'^receptes/create/$', ReceptaCreate.as_view(), name='recepta_create'),
    # ex: /aliments/create/
    url(r'^aliments/create/$', AlimentCreate.as_view(), name='aliment_create'),
    # ex: /metodes/create/
    url(r'^metodes/create/$', MetodeCreate.as_view(), name='metode_create'),  


    # ex: /receptes/1/ingredients/create
    url(r'^receptes/(?P<pk>\d+)/ingredients/create/$',
        IngredientCreate.as_view(),
        name='ingredient_create'),
 
    # ex: /receptes/1/passos/create
    url(r'^receptes/(?P<pk>\d+)/passos/create/$',
        PasCreate.as_view(),
        name='pas_create'),
    # ex: /receptes/1/passos/create
    url(r'^receptes/(?P<pk>\d+)/passos/create/$',
        PasCreate.as_view(),
        name='pas_create'),

#EDICIO PERSONALITZADA
    # ex: /ingredients/1/edit/
    url(r'^ingredients/(?P<pk>\d+)/edit/$', IngredientUpdate.as_view(), name='ingredient_edit'),  
    # ex: /passos/1/edit/
    url(r'^passos/(?P<pk>\d+)/edit/$', PasUpdate.as_view(), name='pas_edit'), 
    # ex: /categories/1/edit/
    url(r'^categories/(?P<pk>\d+)/edit/$', CategoriaUpdate.as_view(), name='categoria_edit'),
    # ex: /receptes/1/edit/
    url(r'^receptes/(?P<pk>\d+)/edit/$', ReceptaUpdate.as_view(), name='recepta_edit'),
    # ex: /aliments/1/edit/
    url(r'^aliments/(?P<pk>\d+)/edit/$', AlimentUpdate.as_view(), name='aliment_edit'),
    # ex: /metodes/1/edit/
    url(r'^metodes/(?P<pk>\d+)/edit/$', MetodeUpdate.as_view(), name='metode_edit'),  

#EDICIO PER DEFECTE
    # ex: /ingredients/1/edit/
   url(r'^ingredients/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = Ingredient,	 template_name = 'form.html',	 form_class = IngredientForm),
	 name='ingredient_edit'), 
    # ex: /passos/1/edit/
   url(r'^passos/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = Pas,	 template_name = 'form.html',	 form_class = PasForm),
	 name='pas_edit'),
    # ex: /categories/1/edit/
   url(r'^categories/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = Categoria,	 template_name = 'form.html',	 form_class = CategoriaForm),	 name='categoria_edit'),
    # ex: /receptes/1/uedit/
   url(r'^receptes/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = Recepta,	 template_name = 'form.html',	 form_class = ReceptaForm),
	 name='recepta_edit'),
    # ex: /aliments/1/edit/
   url(r'^aliments/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = Aliment,	 template_name = 'form.html',	 form_class = AlimentForm),
	 name='aliment_edit'),
    # ex: /metodes/1/edit/
   url(r'^metodes/(?P<pk>\d+)/edit/$',	 UpdateView.as_view(model = MetodePreparacio,	 template_name = 'form.html',	 form_class = MetodePreparacioForm),
	 name='metode_edit'),

#ELIMINACIO
  url(r'^ingredients/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/ingredients',model = Ingredient,template_name = 'delete.html') , 	name='ingredient_delete'),
  url(r'^passos/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/passos',model = Pas,template_name = 'delete.html'),  	name='pas_delete'),
  url(r'^categories/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/categories',model = Categoria,template_name = 'delete.html'),  	name='categoria_delete'),
  url(r'^receptes/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/receptes',model = Recepta,template_name = 'delete.html'),  	name='recepta_delete'),
  url(r'^aliments/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/aliments',model = Aliment,template_name = 'delete.html') ,  name='aliment_delete'),
  url(r'^metodes/(?P<pk>\d+)/delete/$',
  	DeleteView.as_view(success_url = '/metodes',model = MetodePreparacio,template_name = 'delete.html'),  	name='metode_delete'),
 
    # ex: /receptes/1/ingredients/1/edit/
    url(r'^receptes/(?P<pkr>\d+)/ingredients/(?P<pk>\d+)/edit/$',
        IngredientUpdate.as_view(),
        name='dish_edit'),    


#RESTful API

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

