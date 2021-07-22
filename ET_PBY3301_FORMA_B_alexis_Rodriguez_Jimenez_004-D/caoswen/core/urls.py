from django.urls import path
from .views import  home, form_datos, Ver, form_modificar, form_eliminacion, form_Publicacion, lista_datos, lista_api, detalle_datos
from .viewslogin import login

urlpatterns=[ 
    path('', home, name="home"),
    path('lista_api', lista_api, name="lista_api"),
    path('form_datos', form_datos, name="form_datos"),
    path('ver', Ver, name="ver"),
    path('form_modificar/<id>', form_modificar, name="form_modificar"),
    path('form_eliminacion', form_eliminacion, name="form_eliminacion"),
    path('form_Publicacion', form_Publicacion, name="form_Publicacion"),
    path('lista_datos', lista_datos, name="lista_datos"),
    path('login', login, name="login"),
    path('detalle_datos/<id>', detalle_datos, name="detalle_datos"),
    
]