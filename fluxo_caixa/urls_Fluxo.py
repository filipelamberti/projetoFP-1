from django.conf.urls import patterns, include, url

urlpatterns = patterns('fluxo_caixa.views',
    url(r'^$', 'fluxoListar'),
    url(r'^pesquisar/$', 'fluxo_caixa'),
)