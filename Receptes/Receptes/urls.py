from django.conf.urls import patterns, include, url
from iReceptes.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{ 'next_page' : '/'}),
    url(r'^login/$','django.contrib.auth.views.login'),

    #RECEPTES
    url(r'^receptes/$', receptes_list),
    url(r'^receptes/(?P<id>\w+)', recepta_desc),
    
    #INGREDIENTS
    url(r'^ingredients/$', ingredients_list),
    url(r'^ingredients/(?P<ingredient_name>\w+)', ingredient_desc),

    #ALIMENTS
    url(r'^aliments/$', aliments_list),
    #url(r'^aliments/(?P<ingredient_name>\w+)', aliment_desc),

    #CATEGORIES
    url(r'^categories/$', categories_list),
    #url(r'^receptes/(\w+)/$', categoria_desc),
    
    #PASSOS
    url(r'^passos/$', passos_list),
    #url(r'^passos/(?P<ingredient_name>\w+)', pas_desc),

    #METODES PREPARACIO
    url(r'^metodes/$', metodes_list),
    #url(r'^metodes/(?P<ingredient_name>\w+)', metode_desc),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
)
