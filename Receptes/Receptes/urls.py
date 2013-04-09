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
    url(r'^receptes/(?P<recepta_desc>\w+)', recepta_desc),
    url(r'^receptes/recepta/$', recepta_desc),
   # url(r'^receptes/recepta/(?P<id>\w+)/$', recepta_desc , name='recepta desc'),
    url(r'^recepta/recepta/(?P<recepta_name>\w+)', recepta_desc, name = 'recepta desc'),

    #INGREDIENTS
    url(r'^ingredients/', ingredients_list),
    #url(r'^ingredients/(?P<ingredient_name>\w+)/$', ingredient_detail , name='ingredient detail'),
    #url(r'^ingredients/$', ingredient_desc),

    #ALIMENTS
    url(r'^aliments/', aliments_list),

    #CATEGORIA
    #url(r'^categories/', categoria_list),
    #url(r'^receptes/(\w+)/$', categoria_desc),
    #url(r'^receptes/(?P<recepta_name>\w+)/$', categoria_desc, name='categoria desc'),
    #url(r'^recepta/recepta/$', recepta_desc),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
)
