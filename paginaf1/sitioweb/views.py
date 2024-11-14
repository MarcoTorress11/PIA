# sitioweb/views.py
from django.shortcuts import render, redirect
from datetime import date
from django.http import JsonResponse
from .models import RespuestaFormulario
from django.utils import timezone

def index(request):
    contexto = {
        'fecha': date.today()
    }
    return render(request, 'sitioweb/index.html', contexto)

def circuitos(request):
    return render(request, 'sitioweb/circuitos.html')

def escuderias(request):
    return render(request, 'sitioweb/escuderias.html')

def funcionamiento(request):
    return render(request, 'sitioweb/funcionamiento.html')

def pilotos(request):
    return render(request, 'sitioweb/pilotos.html')

def guardar_respuesta(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        duda = request.POST.get('duda')
        fecha = request.POST.get('fecha')
        informacion = request.POST.get('informacion') == 'Sí'
        
        # Guardar en la base de datos
        respuesta = RespuestaFormulario(
            nombre=nombre,
            correo=correo,
            duda=duda,
            fecha=fecha,
            informacion='Sí' if informacion else 'No'
        )
        respuesta.save()
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

# Create your views here.
