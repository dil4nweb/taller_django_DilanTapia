
import json

from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Tarea


@method_decorator(csrf_exempt, name="dispatch")
class ProyectoView(View):

    # GET: consultar todas las tareas o una tarea por ID
    def get(self, request, pk=None):
        if pk is not None:
            try:
                tarea = Tarea.objects.get(pk=pk)
            except Tarea.DoesNotExist:
                return JsonResponse(
                    {"error": "Tarea no encontrada"},
                    status=404
                )

            return JsonResponse({
                "id": tarea.id,
                "titulo": tarea.titulo,
                "descripcion": tarea.descripcion,
                "completada": tarea.completada
            })

        tareas = list(
            Tarea.objects.values(
                "id", "titulo", "descripcion", "completada"
            )
        )

        return JsonResponse({"tareas": tareas})

    # POST: crear una tarea
    def post(self, request):
        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse(
                {"error": "JSON inválido"},
                status=400
            )

        titulo = datos.get("titulo")
        descripcion = datos.get("descripcion", "")
        completada = datos.get("completada", False)

        if not isinstance(titulo, str) or not titulo.strip():
            return JsonResponse(
                {"error": "El título es obligatorio"},
                status=400
            )

        if len(titulo.strip()) > 100:
            return JsonResponse(
                {"error": "El título admite máximo 100 caracteres"},
                status=400
            )

        if not isinstance(descripcion, str):
            return JsonResponse(
                {"error": "La descripción debe ser texto"},
                status=400
            )

        if not isinstance(completada, bool):
            return JsonResponse(
                {"error": "Completada debe ser verdadero o falso"},
                status=400
            )

        tarea = Tarea.objects.create(
            titulo=titulo.strip(),
            descripcion=descripcion,
            completada=completada
        )

        return JsonResponse({
            "mensaje": "Tarea creada correctamente",
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "completada": tarea.completada
        }, status=201)

    # PUT: reemplazar los datos de una tarea existente
    def put(self, request, pk=None):
        if pk is None:
            return JsonResponse(
                {"error": "Se requiere el ID de la tarea"},
                status=400
            )

        try:
            tarea = Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            return JsonResponse(
                {"error": "Tarea no encontrada"},
                status=404
            )

        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse(
                {"error": "JSON inválido"},
                status=400
            )

        titulo = datos.get("titulo")
        descripcion = datos.get("descripcion")
        completada = datos.get("completada")

        if (
            not isinstance(titulo, str)
            or not titulo.strip()
            or len(titulo.strip()) > 100
        ):
            return JsonResponse(
                {"error": "El título es obligatorio y admite "
                          "máximo 100 caracteres"},
                status=400
            )

        if not isinstance(descripcion, str):
            return JsonResponse(
                {"error": "La descripción debe ser texto"},
                status=400
            )

        if not isinstance(completada, bool):
            return JsonResponse(
                {"error": "Completada debe ser verdadero o falso"},
                status=400
            )

        tarea.titulo = titulo.strip()
        tarea.descripcion = descripcion
        tarea.completada = completada
        tarea.save()

        return JsonResponse({
            "mensaje": "Tarea actualizada correctamente",
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "completada": tarea.completada
        })

    # DELETE: eliminar una tarea por ID
    def delete(self, request, pk=None):
        if pk is None:
            return JsonResponse(
                {"error": "Se requiere el ID de la tarea"},
                status=400
            )

        try:
            tarea = Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            return JsonResponse(
                {"error": "Tarea no encontrada"},
                status=404
            )

        tarea.delete()

        return JsonResponse({
            "mensaje": "Tarea eliminada correctamente"
        })
