from django.urls import path
from . import views

app_name = 'docente'  # Definir el espacio de nombres aquí

urlpatterns = [
    path('', views.listar_docentes, name='listar_docentes'),  # Lista de docentes
    path('crear/', views.crear_docente, name='crear_docente'),  # Crear docente
    path('actualizar/<int:pk>/', views.actualizar_docente, name='actualizar_docente'),  # Actualizar docente
    path('eliminar/<int:pk>/', views.eliminar_docente, name='eliminar_docente'),  # Eliminar docente
]
