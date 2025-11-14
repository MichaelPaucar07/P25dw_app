from django.shortcuts import get_object_or_404, render, redirect
from .forms import DocenteForm
from .models import Docente

# Vista para crear un nuevo docente
def crear_docente(request):
    # Si el método de la solicitud es POST, significa que se envió el formulario
    if request.method == "POST":
        # Se llena el formulario con los datos recibidos
        form = DocenteForm(request.POST)

        # Validación del formulario
        if form.is_valid():
            # Si es válido, guarda el nuevo docente en la base de datos
            form.save()
            # Redirecciona a la vista que lista todos los docentes después de guardar
            return redirect(
                "docente:listar_docentes"
            )  # Reemplazar con el nombre correcto de la vista de lista
    else:
        # Si la solicitud es GET, se instancia un formulario vacío
        form = DocenteForm()

    # Renderiza la plantilla para crear un docente, pasando el formulario al contexto
    return render(request, "docente/crear_docente.html", {"form": form})


# Vista para listar todos los docentes
def listar_docentes(request):
    # Recupera todos los docentes de la base de datos
    docentes = Docente.objects.all()

    # Renderiza la plantilla de la lista de docentes, pasando los docentes al contexto
    return render(request, "docente/listar_docentes.html", {"docentes": docentes})


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
    return render(request, "docente/actualizar_docente.html", {"form": form})


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
    return render(request, "docente/eliminar_docente.html", {"docente": docente})
