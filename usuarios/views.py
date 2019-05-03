from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class RegistrarUsuarioView(View):
    
    template_name = 'registrar.html'

    def get(self, request):
        print('Entrei aqui dois')
        return render(request, self.template_name)
    def post(self, request):
        print('Entrei aqui 1')
        return render(request, self.template_name)