from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField('Nombre',max_length=30)
    direccion = models.CharField('Direccion',max_length=80)
    historia = models.CharField('N° Historia',max_length=50, blank=True, null=True)
    genero = models.CharField('Género',max_length=10,blank=True, null=True)
    fecha = models.DateTimeField('Fecha Nacimiento', blank=True, null=True)
    cedula = models.CharField('Cedula',max_length=15,blank=True, null=True)
    representante = models.CharField('Representante',max_length=50, blank=True, null=True)
    telefono_local= models.CharField('Teléfono Local',max_length=15,blank=True, null=True)
    celular = models.CharField('Célular',max_length=15,blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

class Doctores(models.Model):
    nombre = models.CharField('Nombre',max_length=30)
    especialidad = models.CharField('Especialidad',max_length=30)
    telefono_local= models.CharField('Teléfono Local',max_length=15,blank=True, null=True)
    celular = models.CharField('Célular',blank=True,max_length=15, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre


class Consultas(models.Model):
    fecha = models.DateField('Fecha')
    hora = models.CharField('Hora',max_length=5,blank=True, null=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE,related_name='paciente')
    doctor = models.ForeignKey( Doctores, on_delete=models.CASCADE,related_name='doctor')
    status = models.CharField('Status',default='pendiente',max_length=15)
 
    
