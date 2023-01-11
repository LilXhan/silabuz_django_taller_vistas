# Taller views
--- 
Dentro de django, tenemos dos tipos de vista.

- Vistas como funciones
> Estas ya se vieron en los primeros ejemplos

-  Vistas como clases

## Vistas como funciones
--- 
Este tipo de vistas ya las hemos hecho desde que iniciamos la aplicación, con nuestro primer routing.

```python
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Index")
```

Por lo que dentro de nuestras url, lo veríamos de la siguiente forma.

```python
from .views import index_view

urlpatterns = [
    path("", index_view, name="home"),
]
```

Dentro de ellas también podemos añadir una lógica adicional con el tipo de request que se realice.

```python
from django.http import HttpResponse

def index_view(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
    return HttpResponse("Index")
```

Este tipo de implementación es sencilla y muy amigable para vistas pequeñas o que no requieran una lógica compleja, pero que pasa si esta vista sigue escalando en tamaño y complejidad del código.

¿Es sostenible?, no.

Django nos presenta otra forma de crear nuestras vistas. La cual es mediante clases.

## Classes Based Views
--- 
Con esta nueva forma de crear nuestras vistas, podemos reducir la complejidad de nuestro código, ya que los tipos de request van a formar parte de los métodos de la clase.

De esta vista: 

```python
from django.http import HttpResponse

def index_view(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index POST")
    return HttpResponse("Index")
```

Nuestro equivalente en clases sería el siguiente:

```python
from django.views import View
from django.http import HttpResponse

class index_view(View):
    def get(self, request):
        print("GET")
        return HttpResponse("Index")

    def post(self, request):
        print("POST")
        return HttpResponse("Index Post")
```

Django ofrece una clase base para nuestras vistas.

### Añadiendo la clase a las rutas

```python
from .views import index_view

urlpatterns = [
    path("", index_view.as_view()),
]
```

`as_view()` permite volver a la clase en una vista.

## Templates con vistas 
---
También vimos que se puede hacer el renderizado de templates dentro de nuestras vistas.

Tomando el siguiente template, que debe ir en la ruta `myapp/templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Vistas</title>
  </head>
  <body>
    <h1>Nuestra primera vista</h1>
  </body>
</html>
```

Ahora, modificamos nuestra view con función para añadir el render.

```python
from django.shortcuts import render

def index_view(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index POST")
        # Usando el renderizado de un template
    return render(request, "index.html", {})
```

> El tercer parámetro indica el contexto de la aplicación que será explicado posteriormente.

Dentro de la vista hecha con clases, realizamos la siguiente modificación.

```python
# ...
from django.shortcuts import render

class index_view(View):
    # Añadiendo el template como atributo
    template = "index.html"

    def get(self, request):
        print("GET")

        # Usando el renderizado de un template
        return render(request, self.template, {})

    def post(self, request):
        print("POST")
        return HttpResponse("Index Post")
```

## Context
--- 
El contexto de una vista, es la información que es enviada al template para ser mostrada o que se haga uso de ella.

Modificamos `index.html` para poder hacer uso del contexto.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Vistas</title>
  </head>
  <body>
    <h1>{{name}}</h1>
  </body>
</html>
```

Por ejemplo, en la siguiente vista el contexto creado de la siguiente forma:

```python
from django.shortcuts import render

def index_view(request):
    if request.method == "GET":
        print("GET")
    elif request.method == "POST":
        print("POST")
        return HttpResponse("Index POST")
    # Añadiendo el contexto
    context = {}
    context["name"] = "Juan"
    return render(request, "index.html", context)
```

Y en vistas de tipo clases sería de la siguiente forma.

```python
# ...
class index_view(View):
    template = "index.html"

    #Creando el contexto
    context = {"name": "Juan"}
    def get(self, request):
        print("GET")

        # Enviando el contexto
        return render(request, self.template, self.context)

    def post(self, request):
        print("POST")
        return HttpResponse("Index Post")
```

## Tarea 
--- 
Crear dos vistas en forma de función y clase.

> Tomar en cuenta que para ambas vistas deben crear un template en el se renderize la información.

### Vista 1

Contexto: name y edad

```sample
Hola, me llamo {{name}} y tengo {{edad}} años.
```

##### Tipos de datos

-   name: string
-   edad: Date

##### Consideraciones 

En la vista, `{{edad}}` es un campo que debe ser calculado en base a la fecha de nacimiento.

Porque, normalmente en todas las bases únicamente se almacena la fecha de nacimiento del usuario y no su edad como tal. Debido a que, este valor depende de la fecha de consulta.

Por ejemplo: No es lo mismo ver la edad en el 2020 que en el 2022.

### Vista 2

Contexto: name y lista de números de 1 al 4.

```sample
La numeración para {{name}} es la siguiente:

- 1
- 2
- 3
- 4
```

##### Tipos de datos

-   name: string
-   lista de números: `array[int]`

Links PPT:  [Diapositivas](https://docs.google.com/presentation/d/e/2PACX-1vSn3IzFUz9cNcJwDeDZK2F48JlEZ-2wu5AxF6V66gh253XfIEd-DcHMAZjpkSAHuiezakzkeL1levuD/embed?start=false&loop=false&delayms=3000&slide=id.g16b26a04f67_0_0)
Links Youtube:
- [Teoria](https://www.youtube.com/watch?v=ke_lu-UTjn4&list=PLxI5H7lUXWhjV-yCSEuJXxsDmNESrvbw3&index=6&ab_channel=Silabuz)
- [Practica](https://www.youtube.com/watch?v=t2KwCKvqATg&list=PLxI5H7lUXWhjV-yCSEuJXxsDmNESrvbw3&index=7&ab_channel=Silabuz)
