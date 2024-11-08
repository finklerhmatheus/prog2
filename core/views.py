from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request,'contato.html')

def pedido(request):
    return render(request,'pedido.html')

'''
def produto(request, pk):
    print(f'PK: {pk}')
    return render(request,'produto.html')
'''

def produto(request, pk):
    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)