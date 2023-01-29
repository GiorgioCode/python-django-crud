from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.
def home(request):
    curso = Curso.objects.all()
    return render(request, "gestionCursos.html",{"cursos":curso})


def registrarCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    creditos=request.POST['creditos']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def editarCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    creditos=request.POST['creditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect("/")

def eliminacionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def edicionCurso(request,codigo):
    cursos = Curso.objects.all()
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html",{"curso":curso , "cursos":cursos})
