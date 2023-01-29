from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('registrarCurso/', views.registrarCurso),
    path('eliminacionCurso/<codigo>',views.eliminacionCurso),
    path('edicionCurso/<codigo>',views.edicionCurso),
    path('editarCurso/',views.editarCurso)
]
