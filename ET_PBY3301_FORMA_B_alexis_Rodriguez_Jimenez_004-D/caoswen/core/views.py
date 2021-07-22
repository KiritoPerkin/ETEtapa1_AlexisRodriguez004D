from django.shortcuts import render, redirect
from django.views.decorators import csrf
from rest_framework.serializers import Serializer
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

from rest_framework.serializers import Serializer
from rest_framework import status
from django.views.decorators import csrf
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import datosSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def lista_datos(request): 
    if request.method== 'GET':
        datos = datos.objects.all()
        serializer =datosSerializer(datos, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = datosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def lista_api(request):
    return render(request, 'ApiWeb.html')

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_datos(request,id): 
    try: 
        datos = datos.objects.get(patente=id) 
    except datos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': 
        serializer = datosSerializer(vehiculo)
        return Response(serializer.data)
    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = datosSerializer(datos, data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE': 
        datos.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)