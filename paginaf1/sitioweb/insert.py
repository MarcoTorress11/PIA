# sitioweb/views.py
from .models import RespuestaFormulario

# Guardar en la base de datos
respuesta = RespuestaFormulario(
    nombre='Marco',
    correo='test@tes.com',
    duda='Test1',
    fecha='01-02-2024',
    informacion='Si'
)
respuesta.save()

