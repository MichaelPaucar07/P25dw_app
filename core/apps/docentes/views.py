from django.shortcuts import get_object_or_404, render, redirect
from .forms import DocenteForm
from .models import Docente

# Funcion crear un nuevo docente
def crear_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            docente = form.save()
            if docente.imagen:
                print(f"Imagen cargada correctamente: {docente.imagen.name}")
            else:
                print("No se cargó la imagen")

            return redirect("docente:listar_docentes")
    else:
        form = DocenteForm()
    return render(request, "crear_docente.html", {"form": form})

# Funcion listar todos los docentes
def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request, "listar_docentes.html", {"docentes": docentes})

# Funcion actualizar docentes
def actualizar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect("docente:listar_docentes")
    else:
        form = DocenteForm(instance=docente)
    return render(request, "actualizar_docente.html", {"form": form, "docente": docente})

# Funcion eliminar docentes
def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        docente.delete()
        return redirect(
            "docente:listar_docentes"
        )
    return render(request, "eliminar_docente.html", {"docente": docente})
