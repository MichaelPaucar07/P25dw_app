from django.shortcuts import render, redirect, get_object_or_404
from .models import Materias
from .forms import MateriasForm

# Funcion crear una nueva materia
def crear_materia(request):
    if request.method == "POST":
        form = MateriasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "materia:listar_materias"
            )
    else:
        form = MateriasForm()
    return render(request, "crear_materia.html", {"form": form})

# Funcion listar todas las materias
def listar_materias(request):
    materias = Materias.objects.all()
    return render(request, "listar_materias.html", {"materias": materias})


# Funcion actualizar materias
def actualizar_materia(request, pk):
    materia = get_object_or_404(Materias, pk=pk)
    if request.method == "POST":
        form = MateriasForm(request.POST, request.FILES, instance=materia)
        if form.is_valid():
            form.save()
            return redirect("materia:listar_materias")
    else:
        form = MateriasForm(instance=materia)
    return render(request, "actualizar_materia.html", {
        "form": form,
        "materia": materia
    })

# Funcion para eliminar materias
def eliminar_materia(request, pk):
    materia = get_object_or_404(
        Materias, pk=pk
    )
    if request.method == "POST":
        materia.delete()
        return redirect(
            "materia:listar_materias"
        )
    return render(request, "eliminar_materia.html", {"materia": materia})