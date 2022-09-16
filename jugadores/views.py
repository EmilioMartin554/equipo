from django.shortcuts import render
from jugadores.forms import plantelFormulario
from django.http import HttpResponse
from .models import Plantel
def insertar_jugador(request):
    if request.method == "POST":

            formulario = plantelFormulario(request.POST)
            print(formulario)
            if formulario.is_valid():
                formulario=formulario.cleaned_data
                jugador = Plantel(nombre=formulario["nombre"],edad=formulario["edad"],posicion=formulario["posicion"],peso=formulario["peso"],goles=formulario["goles"])
                jugador.save()
                archivo = open(f"{jugador.nombre}{jugador.id}.txt","w")
                archivo.write(f"Nombre: {jugador.nombre}\nEdad: {jugador.edad}\nPosicion: {jugador.posicion}\nPeso: {jugador.peso}\nGoles: {jugador.goles}")
                archivo.close()
            
                return render(request, "insertar_jugadores.html")
                
    return render(request, "insertar_jugadores.html")
def leer_jugadores(request):
    jugadores=Plantel.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request,"leer_jugadores.html",contexto)

def buscar(request):
    if request.method == "POST":
        nombre=request.POST["nombre"]
        jugador = Plantel.objects.filter(nombre__contains=nombre)
        return render(request,"buscar.html",{"jugadores":jugador})
    return render(request,"buscar.html")

# Create your views here.
def eliminar(request, id):
    jugador=Plantel.objects.get(id=id)
    jugador.delete()
    jugadores = Plantel.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request,"leer_jugadores.html",contexto)
def editar(request,id):
    jugador=Plantel.objects.get(id=id)
    if request.method == "POST":
        form=plantelFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            jugador.nombre=info["nombre"]
            jugador.edad=info["edad"]
            jugador.posicion=info["posicion"]
            jugador.peso=info["peso"]
            jugador.goles=info["goles"]
            archivo = open(f"{jugador.nombre}{jugador.id}.txt","w")
            archivo.write(f"Nombre: {jugador.nombre}\nEdad: {jugador.edad}\nPosicion: {jugador.posicion}\nPeso: {jugador.peso}\nGoles: {jugador.goles}")
            archivo.close()
            jugador.save()
            jugador=Plantel.objects.all()
            return render(request,"leer_jugadores.html",{"jugadores":jugador})
    else:
        form=plantelFormulario(initial={"nombre":jugador.nombre,"edad":jugador.edad,"posicion":jugador.posicion,"peso":jugador.peso,"goles":jugador.goles})
#        archivo = open(f"{jugador.nombre}{jugador.id}.txt","w")
#        archivo.write(f"Nombre: {jugador.nombre}\nEdad: {jugador.edad}\nPosicion: {jugador.posicion}\nPeso: {jugador.peso}\nGoles: {jugador.goles}")
#        archivo.close()
        return render(request,"editar_jugadores.html",{"formulario":form,"jugador":jugador})