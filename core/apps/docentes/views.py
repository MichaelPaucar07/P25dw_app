from django.shortcuts import get_object_or_404, render, redirect
from .forms import DocenteForm
from .models import Docente

# Vista para crear un nuevo docente
def crear_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES)  # Asegúrate de que se pasan los archivos

        if form.is_valid():
            # Si el formulario es válido, guardamos el docente
            docente = form.save()

            # Verifica si la imagen fue cargada correctamente
            if docente.imagen:
                print(f"Imagen cargada correctamente: {docente.imagen.name}")
            else:
                print("No se cargó la imagen")

            return redirect("docente:listar_docentes")
    else:
        form = DocenteForm()

    return render(request, "crear_docente.html", {"form": form})



# Vista para listar todos los docentes
def listar_docentes(request):
    # Recupera todos los docentes de la base de datos
    docentes = Docente.objects.all()

    # Renderiza la plantilla de la lista de docentes, pasando los docentes al contexto
    return render(request, "listar_docentes.html", {"docentes": docentes})


# Vista para actualizar un docente
def actualizar_docente(request, pk):
    # Obtiene el docente con el ID proporcionado
    docente = get_object_or_404(Docente, pk=pk)

    # Si el método de la solicitud es POST, significa que se envió el formulario con datos
    if request.method == "POST":
        form = DocenteForm(request.POST, instance=docente)

        # Validación del formulario
        if form.is_valid():
            # Guarda los cambios en el docente
            form.save()
            # Redirige a la vista de lista de docentes
            return redirect(
                "docente:listar_docentes"
            )  # Reemplazar con el nombre correcto de la vista
    else:
        # Si la solicitud es GET, se rellena el formulario con los datos actuales del docente
        form = DocenteForm(instance=docente)

    # Renderiza la plantilla para actualizar un docente, pasando el formulario al contexto
    return render(request, "actualizar_docente.html", {"form": form})


# Vista para eliminar un docente
def eliminar_docente(request, pk):
    # Obtiene el docente con el ID proporcionado
    docente = get_object_or_404(Docente, pk=pk)

    # Si la solicitud es POST, se confirma la eliminación
    if request.method == "POST":
        # Elimina el docente de la base de datos
        docente.delete()
        # Redirige a la lista de docentes después de eliminar
        return redirect(
            "docente:listar_docentes"
        )  # Reemplazar con el nombre correcto de la vista

    # Si la solicitud es GET, muestra la confirmación de eliminación
    return render(request, "eliminar_docente.html", {"docente": docente})
