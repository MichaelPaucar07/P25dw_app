from django.shortcuts import render, redirect, get_object_or_404
from .models import Materias
from .forms import MateriasForm

# Vista para crear una nueva materia
def crear_materia(request):
    if request.method == "POST":
        form = MateriasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "materia:listar_materias"
            )  # Redirige a la lista de materias después de guardar
    else:
        form = MateriasForm()  # Si es GET, muestra un formulario vacío

    return render(request, "materia/crear_materia.html", {"form": form})


# Vista para listar todas las materias
def listar_materias(request):
    materias = Materias.objects.all()  # Recupera todas las materias de la base de datos
    return render(request, "materia/listar_materias.html", {"materias": materias})


# Vista para actualizar una materia existente
def actualizar_materia(request, pk):
    materia = get_object_or_404(
        Materias, pk=pk
    )  # Obtiene la materia con el ID proporcionado
    if request.method == "POST":
        form = MateriasForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect(
                "materia:listar_materias"
            )  # Redirige a la lista de materias después de guardar los cambios
    else:
        form = MateriasForm(
            instance=materia
        )  # Si es GET, rellena el formulario con los datos actuales de la materia

    return render(request, "materia/actualizar_materia.html", {"form": form})


# Vista para eliminar una materia
def eliminar_materia(request, pk):
    materia = get_object_or_404(
        Materias, pk=pk
    )  # Obtiene la materia con el ID proporcionado
    if request.method == "POST":
        materia.delete()  # Elimina la materia de la base de datos
        return redirect(
            "materia:listar_materias"
        )  # Redirige a la lista de materias después de eliminar

    return render(request, "materia/eliminar_materia.html", {"materia": materia})