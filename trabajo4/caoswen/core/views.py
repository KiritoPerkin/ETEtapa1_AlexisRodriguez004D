from django.shortcuts import render, redirect
from .models import datos,Publicacion
from .forms import datosForm,PublicacionForm


# Create your views here.
def home(request):
    nombre = ''

    datosForm = datos.objects.all()    

    return render(request, 'home.html', context={'nombre_usuario':nombre,'datos':datos})

def form_datos(request):
    if request.method == 'POST': 
        datos_form = datosForm(request.POST)
        if datos_form.is_valid():
            datos_form.save()        
            return redirect('home')
    else: 
        datos_form = datosForm()
    return render(request, 'core/form_crear.html', {'datos_form': datos_form})

def Ver(request):
    datosForm = datos.objects.all()

    return render(request, 'core/ver.html', {'datos': datos})

def form_modificar(request, id):
    datosForm = datos.objects.get(rutcola=id)

    datos ={
        'form': datosForm(instance=datos)
    }
    if request.method == 'POST': 
        formulario = datosForm(data=request.POST, instance = datos)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_modificar.html', datos)

def form_eliminacion(request,id):
    datosForm = datos.objects.get(rutcola=id)
    datos.delete()
    return redirect('ver')

def form_Publicacion(request):
    if request.method == 'POST': 
        Publicacion_form = PublicacionForm(request.POST)
        if Publicacion_form.is_valid():
            Publicacion_form.save()        
            return redirect('home')
    else: 
        Publicacion_form = PublicacionForm()
    return render(request, 'core/form_Publicacion.html', {'Publicacion_form': Publicacion_form})
