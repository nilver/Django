from django import  forms
from .models import Pacientes, Doctores, Consultas


TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)



class PacienteForm(forms.Form):
    model = Pacientes
