from datetime import datetime
import csv, operator
from unidad.models import Pacientes

print("Comienzo")
with open('b.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for row in entrada:
        nombre=row[0]
        fecha=row[1]
        cedula=row[2]
        historia=row[2]
        edad= row[3]
        genero=row[4]
        direccion=row[5]
        diag=row[6]
        rep=row[7]
        local=row[8]
        date = datetime.strptime(fecha, "%m/%d/%Y")
        datetime.strftime(date, "%Y-%m-%d")
        p=Pacientes(nombre=nombre,direccion=direccion,historia=historia,genero=genero,fecha=date,cedula=cedula,edad=edad,representante=rep,telefono_local=local,diagnostico=diag)
        p.save()
print("Final")
