from django.shortcuts import render
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
	pessoas = Pessoa.objects.all().order_by('nome')
	return render(request, 'fluxo_caixa/lista_fluxo.html', {'pessoas': pessoas} )

def fluxoPesquisar(request):
    if request.method == 'POST':

        data_Inicial = request.POST.get('data_Inicial', '%d/%m/%Y')
        data_Final = request.POST.get('data_Final', '%d/%m/%Y')
        total = 0

       
        contas = Conta.objects.filter(data__range=(data_Inicial, data_Final))
        for conta in contas:
            total += conta.valor
        
        contas = []

        return render(request, 'fluxo_caixa/lista_fluxo.html', {'contas': contas, 'total': total, 'data_Inicial': data_Inicial, 'data_Final': data_Final})
    
    return render(request, 'fluxo_caixa/lista_fluxo.html', {'contas': []})

