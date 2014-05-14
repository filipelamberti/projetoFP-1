from django.shortcuts import render
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
	pessoas = Pessoa.objects.all().order_by('nome')
	return render(request, 'fluxo_caixa/lista_fluxo.html', {'pessoas': pessoas} )

