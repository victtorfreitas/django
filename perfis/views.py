from django.shortcuts import render,redirect
from perfis.models import Perfil

def index (request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})
def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    if perfil is None:
        print('Entrei aqui')
        perfil = Perfil()
        
    return render(request, 'perfis.html', {'perfil': perfil})

def convidar(request, perfil_id):
    perfil_convidado = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convidado)
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)