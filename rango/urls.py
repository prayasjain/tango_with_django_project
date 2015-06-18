from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^about$',views.about,name='about'))

# urlpatterns name fixed. It is a tuple saying if the url matches the regex open the particular view name is option for
#our convenience