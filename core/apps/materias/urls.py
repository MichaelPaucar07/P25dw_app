from django.urls import path
from . import views

app_name = 'materia'  # Aquí definimos el espacio de nombres

urlpatterns = [
    path('', views.listar_materias, name='listar_materias'),
    path('crear/', views.crear_materia, name='crear_materia'),
    path('actualizar/<int:pk>/', views.actualizar_materia, name='actualizar_materia'),
    path('eliminar/<int:pk>/', views.eliminar_materia, name='eliminar_materia'),
]
