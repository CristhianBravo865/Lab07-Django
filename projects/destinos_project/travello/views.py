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