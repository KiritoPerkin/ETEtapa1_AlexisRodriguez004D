from django.urls import path
from .views import  home, form_datos, Ver, form_modificar, form_eliminacion,form_Publicacion

urlpatterns=[ 
    path('', home, name="home"),
    path('form_datos', form_datos, name="form_datos"),
    path('ver', Ver, name="ver"),
    path('form_modificar/<id>', form_modificar, name="form_modificar"),
    path('form_eliminacion', form_eliminacion, name="form_eliminacion"),
    path('form_Publicacion', form_Publicacion, name="form_Publicacion")

]