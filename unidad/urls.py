from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^pacientes/buscar$', views.PacienteBuscar, name='pacienteBuscar'),
    url(r'^pacientes$', views.PacientesList.as_view(), name='list'),
    url(r'^pacientes/(?P<pk>\d+)$', views.PacientesDetail.as_view(), name='detail'),
    url(r'^pacientes/nuevo$', views.PacientesCreation.as_view(), name='new'),
    url(r'^pacientes/editar/(?P<pk>\d+)$', views.PacientesUpdate.as_view(), name='edit'),
 
    url(r'^personal$', views.PersonalList.as_view(), name='personalList'),
    url(r'^personal/(?P<pk>\d+)$', views.PersonalDetail.as_view(), name='personalDetail'),
    url(r'^personal/nuevo$', views.PersonalCreation.as_view(), name='personalNew'),
    url(r'^personal/editar/(?P<pk>\d+)$', views.PersonalUpdate.as_view(), name='personalEdit'),
    url(r'^pacientes/consultaNueva/(?P<paciente_id>\d+)$', views.ConsultaNueva, name='consultaNueva'),
 
    url(r'^consultas$', views.ConsultasList.as_view(), name='consultasList'),
    url(r'^consultas/editarStatus/(?P<consulta_id>\d+)$', views.EditStatus, name='editStatus'),
    url(r'^consultas/buscar$', views.ConsultaBuscar, name='consultaBuscar'),
    
    
]    

