from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render,render_to_response
from django.urls import reverse,reverse_lazy
from django.db.models import Q


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Pacientes,Doctores,Consultas




def index(request):
    return render(request, 'base.html')

def PacienteBuscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(historia__icontains=query) 
        )
        results = Pacientes.objects.filter(qset)
        #print(results)
    else:
        results = []
    return render_to_response('unidad/pacientes_list.html', {
        "results": results,
        "query": query
    })


def EditStatus(request,consulta_id):

    status = request.POST.get('q', '')
    
    if request.method== "POST":
        value=request.POST.get('status')
        c1 = Consultas.objects.get(id=consulta_id)
        c1.status=value
        c1.save()
        return render(request, 'base.html')
    else:
        consulta = get_object_or_404(Consultas, pk=consulta_id)
        context = {'consulta': consulta}
        return render(request, 'unidad/consultas_status.html', context)

def ConsultaNueva(request,paciente_id):
    doctores = Doctores.objects.all()
    paciente = get_object_or_404(Pacientes, pk=paciente_id)
    context = {'doctores': doctores, 'paciente':paciente}
    return render(request, 'unidad/consultas_nueva.html', context)


def CrearConsulta(request,paciente_id):
    doctores = Doctores.objects.all()
    context = {'doctores': doctores}
    return render(request, 'unidad/pacientes_list.html', context)

class PacientesList(ListView):
    model = Pacientes


class PacientesDetail(DetailView):
    model = Pacientes


class PacientesCreation(CreateView):
    model = Pacientes
    success_url = reverse_lazy('list')
    fields = ['nombre', 'historia', 'direccion', 'genero']


class PacientesUpdate(UpdateView):
    model = Pacientes
    success_url = reverse_lazy('list')
    fields = ['nombre', 'historia', 'direccion', 'genero']


class PersonalList(ListView):
    model = Doctores

class PersonalDetail(DetailView):
    model = Doctores


class PersonalCreation(CreateView):
    model = Doctores
    success_url = reverse_lazy('personalList')
    fields = ['nombre', 'especialidad', 'telefono_local', 'celular']


class PersonalUpdate(UpdateView):
    model = Doctores
    success_url = reverse_lazy('personalList')
    fields = ['nombre', 'especialidad', 'telefono_local', 'celular']


class ConsultasList(ListView):
    model = Consultas