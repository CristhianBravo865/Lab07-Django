from django.shortcuts import render, redirect
from .models import DestinosTuristicos
# Create your views here.


def index(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'destinos': destinos})
def add_destination(request):
    if request.method == 'POST':
        nombreCiudad = request.POST.get('nombreCiudad')
        descripcionCiudad = request.POST.get('descripcionCiudad')
        imagenCiudad = request.FILES.get('imagenCiudad')
        precioTour = request.POST.get('precioTour')
        ofertaTour = request.POST.get('ofertaTour') == 'on'

        destino = DestinosTuristicos(
            nombreCiudad=nombreCiudad,
            descripcionCiudad=descripcionCiudad,
            imagenCiudad=imagenCiudad,
            precioTour=precioTour,
            ofertaTour=ofertaTour
        )
        destino.save()
        return redirect('list_destinations')

    return render(request, 'add_destination.html')

def list_destinations(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'list_destinations.html', {'destinos': destinos})

def edit_destination(request, id):
    destino = DestinosTuristicos.objects.get(id=id)

    if request.method == 'POST':
        destino.nombreCiudad = request.POST.get('nombreCiudad')
        destino.descripcionCiudad = request.POST.get('descripcionCiudad')
        if request.FILES.get('imagenCiudad'):
            destino.imagenCiudad = request.FILES.get('imagenCiudad')
        destino.precioTour = request.POST.get('precioTour')
        destino.ofertaTour = request.POST.get('ofertaTour') == 'on'
        destino.save()
        return redirect('list_destinations')

    return render(request, 'edit_destination.html', {'destino': destino})

def delete_destination(request, id):
    destino = DestinosTuristicos.objects.get(id=id)
    destino.delete()
    return redirect('list_destinations')