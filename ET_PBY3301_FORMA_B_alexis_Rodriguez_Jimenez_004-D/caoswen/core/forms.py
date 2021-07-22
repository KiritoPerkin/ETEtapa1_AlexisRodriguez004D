from django import forms
from django.forms.models import ModelChoiceField
from django.forms import ModelForm,widgets 
from .models import datos,Publicacion

class datosForm(ModelForm):

    class Meta:
        model = datos
        fields = ['rut', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'contrasena']

        labels={
            'rut': 'rut colaborador: ',
            'nombre': 'nombre: ',
            'telefono': 'telefono: ',
            'direccion': 'direccion: ',
            'email': 'email: ',
            'pais': 'pais: ',
            'contrasena': 'contrasena: ',
        
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rutcola', 
                    'name': 'rut',
                    'placeholder': 'Digite rut'
                }
            ),
            'nombre ': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre', 
                    'name': 'nombre',
                    'placeholder': 'Digite nombre'

                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                    'name': 'telefono', 
                    'placeholder': 'Digite telefono'

                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'name': 'direccion', 
                    'placeholder': 'Digite direccion'

                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email', 
                    'name': 'email',
                    'placeholder': 'Digite email'

                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'pais',
                    'name': 'pais', 
                    'placeholder': 'Digite pais'

                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contrasena',
                    'name': 'contrasena', 
                    'placeholder': 'Digite contrasena'

                }
            )
        }
class PublicacionForm(ModelForm):

    class Meta:
        model = Publicacion
        fields = ['Correo', 'Nombre', 'Detalles', 'rut']

        labels={
            'Correo': 'Correo: ',
            'Nombre': 'nombre: ',
            'Detalles': 'Detalles: ',
            'rut': 'Rut: ',

        
        }
        widgets={
            'Correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Correo', 
                    'name': 'Correo',
                    'placeholder': 'Digite correo'
                }
            ),
            'Nombre ': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre', 
                    'name': 'nombre',
                    'placeholder': 'Digite nombre'

                }
            ), 
            'Detalles': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Detalles',
                    'name': 'Detalles', 
                    'placeholder': 'Digite detalles de publicacion'

                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut', 
                    'placeholder': 'Digite rut'

                }
            )
            
        }