
from django.urls import path
from .views import ProyectoView


urlpatterns = [
    path(
        "tareas/",
        ProyectoView.as_view(),
        name="lista_tareas"
    ),
    path(
        "tareas/<int:pk>/",
        ProyectoView.as_view(),
        name="detalle_tarea"
    ),
]
