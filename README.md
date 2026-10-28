# Taller - Peticiones en django

Estudiante: Dilan De Jesus Tapia Mercado

---

Construir endpoints de manera nativa en Django significa desarrollar APIs REST sin utilizar librerias externas pesadas (como Django REST Framework), aprovechando unicamente las herramientas que provee el nucleo del framework.

### 1. Verbos HTTP y su Relacion con las Operaciones CRUD

Mediante una Vista Basada en Clase (View), los metodos gestionan las peticiones segun el estandar REST:

* **get() -> Read (Leer):** Solicita y recupera recursos del servidor. Puede consultar la lista completa de registros o filtrar el detalle de un elemento especifico mediante su identificador (pk).
* **post() -> Create (Crear):** Envia nuevos datos desde el cliente para que el servidor los procese y registre un nuevo elemento en la base de datos.
* **put() -> Update (Actualizar):** Modifica o reemplaza por completo un recurso ya existente utilizando su identificador (pk).
* **delete() -> Delete (Eliminar):** Solicita la eliminacion de un recurso especifico de la base de datos a partir de su identificador (pk).

---

### 2. Modulos, Funciones y Decoradores de Django Utilizados

* **django.views.View:** Clase base para crear vistas orientadas a objetos, permitiendo separar la logica por metodos HTTP (get, post, put, delete).
* **django.http.JsonResponse:** Convierte diccionarios y listas de Python en una respuesta HTTP con formato JSON (Content-Type: application/json).
* **django.views.decorators.csrf.csrf_exempt:** Decorador que deshabilita temporalmente la proteccion contra falsificacion de peticion en sitios cruzados (CSRF), permitiendo pruebas exitosas de metodos POST, PUT y DELETE desde clientes externos.
* **django.utils.decorators.method_decorator:** Permite aplicar decoradores orientados a funciones (como csrf_exempt) a metodos dentro de una vista basada en clases.
* **json.loads (Modulo estandar de Python):** Se utiliza en conjunto con request.body para deserializar el cuerpo de las peticiones HTTP enviadas en formato JSON.

---

### Fuentes

* **Documentacion Oficial de Django:** Vistas basadas en clases y Objetos de peticion/respuesta (HttpRequest y HttpResponse). [https://docs.djangoproject.com/es/](https://docs.djangoproject.com/es/)
* **MDN Web Docs (Mozilla Developer Network):** Tutorial de Django: Listas genéricas y Vistas basadas en clases. [https://developer.mozilla.org/es/docs/Learn/Server-side/Django](https://developer.mozilla.org/es/docs/Learn/Server-side/Django)
