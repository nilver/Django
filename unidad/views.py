from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render,render_to_response
from django.urls import reverse,reverse_lazy
from django.db.models import Q
from datetime import datetime

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



def ConsultaBuscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(paciente__nombre__icontains=query) |
            Q(paciente__historia__icontains=query) 
        )
        results = Consultas.objects.filter(qset)
        #print(results)
    else:
        results = []
    return render_to_response('unidad/consultas_list.html', {
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

    if request.method== "POST":
        
        doctor=request.POST.get('doctor')
        p1 = Pacientes.objects.get(id=paciente_id)
        d1 = Doctores.objects.get(id=doctor)
        fecha=request.POST.get('fecha')
        hora=request.POST.get('hora')
        date = datetime.strptime(fecha, "%d/%m/%Y")
        datetime.strftime(date, "%Y-%m-%d")
       
        doctor=paciente_id
        Consultas.objects.create(paciente=p1,doctor=d1,fecha=date,hora=hora)
        return render(request, 'base.html')
    
    else:    
        doctores = Doctores.objects.all()
        paciente = get_object_or_404(Pacientes, pk=paciente_id)
        context = {'doctores': doctores, 'paciente':paciente}
        return render(request, 'unidad/consultas_nueva.html', context)





#UN um
def CrearConsulta(request,paciente_id):
    doctores = Doctores.objects.all()
    context = {'doctores': doctores}
    return render(request, 'unidad/pacientes_list.html', context)

class ConsultasList(ListView):
    model = Consultas


#Pacientes

def PacienteBuscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(historia__icontains=query) 
        )
        results = Pacientes.objects.filter(qset)
        print(results)
    else:
        results = []
    return render_to_response('unidad/pacientes_list.html', {
        "results": results,
        "query": query
    })


class PacientesList(ListView):
    model = Pacientes


class PacientesDetail(DetailView):
    model = Pacientes


class PacientesCreation(CreateView):
    model = Pacientes
    success_url = reverse_lazy('list')
    fields = ['nombre', 'historia', 'genero','fecha','direccion','cedula','representante','telefono_local','celular','diagnostico','edad']

class PacientesUpdate(UpdateView):
    model = Pacientes
    success_url = reverse_lazy('list')
    fields = ['nombre', 'historia', 'genero','fecha','direccion','cedula','representante','telefono_local','celular','diagnostico','edad']

# Personal


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

