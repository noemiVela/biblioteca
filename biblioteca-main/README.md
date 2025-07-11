 # 📚 Aplicación Web para Gestión y Análisis de Libros

Bienvenida al proyecto 🎉. Este sistema web, desarrollado con **Python** y **Django**, facilita el manejo de información sobre libros, autores y géneros. Además, permite analizar datos y crear gráficos para visualizar estadísticas de lectura.

---

## ✅ Entorno y Tecnologías

```python
Python >= 3.10
Django >= 4.2
PostgreSQL >= 14
Pandas >= 1.5
Matplotlib >= 3.6
Seaborn >= 0.12
Scikit-learn >= 1.2
Virtualenv >= 20
```

⚙️ Puesta en Marcha

1. Crear un entorno virtual
```python
python -m venv venv
```
2. Activar el entorno

En Windows:
```python
venv\Scripts\activate
```

En Linux/macOS:
```python
source venv/bin/activate
```

3. Instalar dependencias
```python
pip install django pandas matplotlib seaborn scikit-learn psycopg2-binary
```

🎯 Configuración de Base de Datos

Para conectar Django a PostgreSQL, modifica settings.py así:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'libreria_db',
        'USER': 'postgres',
        'PASSWORD': 'sdasddas',
        'HOST': 'localhost',
        'PORT': '7833',
    }
}
```

📖 Funcionalidades Principales

Con esta app podrás:

✅ Registrar información de autores, géneros y libros.

✅ Consultar registros de libros existentes.

✅ Obtener sugerencias de lectura por género, basadas en calificaciones.

✅ Generar gráficos para analizar datos de la biblioteca.

✅ Gestión de Autores

Modelo Author
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

Vista para registrar autores
```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Author

@csrf_exempt
def add_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        author = Author.objects.create(name=data['name'])
        return JsonResponse({'message': 'Autor creado', 'id': author.id})
```

Ejemplo en Postman:

<img width="929" height="412" alt="image" src="https://github.com/user-attachments/assets/ac1dea5c-0940-41e3-a48a-ec38a7ab8418" />

✅ Gestión de Géneros

Modelo Generos
```python
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

Vista para crear un género
```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Genre

@csrf_exempt
def add_genre(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        genre = Genre.objects.create(name=data['name'])
        return JsonResponse({'message': 'Género creado', 'id': genre.id})
```

Ejemplo en Postman:

<img width="924" height="382" alt="image" src="https://github.com/user-attachments/assets/89633cf6-3766-4a58-b605-26752a83de38" />

✅ Registro de Libros

Vista para agregar libros
```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            year=data['year'],
            rating=data['rating']
        )
        return JsonResponse({'message': 'Libro creado', 'id': book.id})
```

Ejemplo en Postman:

<img width="931" height="535" alt="image" src="https://github.com/user-attachments/assets/524543f7-bfff-401b-8ed1-d63637445266" />

✅ Visualización de Libros

Vista para listar todos los libros
```python
from django.http import JsonResponse
from .models import Book

def list_books(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)
```

Ejemplo en Postman:

<img width="931" height="429" alt="image" src="https://github.com/user-attachments/assets/48d7275a-10b1-48eb-82ba-d5944ef8fa8b" />

✅ Actualización de Calificaciones

Vista para actualizar la puntuación de un libro
```python
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Book

@csrf_exempt
def rate_book(request, book_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(id=book_id)
        book.rating = data['rating']
        book.save()
        return JsonResponse({'message': 'Calificación actualizada', 'rating': book.rating})
```

Ejemplo en Postman:

<img width="922" height="408" alt="image" src="https://github.com/user-attachments/assets/5f98ecac-eeaf-4ab0-bbb4-02a8d5b00d01" />

📝 Lectura de Datos con Pandas

Para análisis de datos, puedes usar este script para leer datos de la base:
```python
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname='libreria_db',
    user='postgres',
    password='tu_password',
    host='localhost',
    port='5432'
)

query = "SELECT * FROM libros_book;"
df = pd.read_sql(query, conn)

print(df.head())
```

📊 Análisis Visual

Distribución de las calificaciones:

<img width="970" height="577" alt="image" src="https://github.com/user-attachments/assets/85018a5b-82b5-447a-92e4-6f077da1a9bd" />

Promedio de calificación por usuario:

<img width="965" height="571" alt="image" src="https://github.com/user-attachments/assets/2ba0ba85-e9cb-4c15-b2da-b4c1a239ea90" />

Cantidad de libros en cada género:

<img width="586" height="584" alt="image" src="https://github.com/user-attachments/assets/be7d33c2-a723-4d68-8819-12992544c9c9" />

Autores más prolíficos

(imagen del gráfico autores más prolíficos)

Libros con mejor promedio de calificación

<img width="966" height="479" alt="image" src="https://github.com/user-attachments/assets/86e4cfa0-ab1d-401e-a164-e16ce986d77e" />

Media de valoración por género

<img width="963" height="570" alt="image" src="https://github.com/user-attachments/assets/ed0defc8-93b2-4563-9bf1-21be744786b1" />

Libros más valorados

<img width="966" height="571" alt="image" src="https://github.com/user-attachments/assets/d581bde2-dbe1-4025-a78a-5d1299940699" />

Autores con más calificaciones

<img width="967" height="576" alt="image" src="https://github.com/user-attachments/assets/b29961ee-fecc-4e08-9dfb-13bb6d745592" />

Evolución de publicaciones a lo largo de los años

<img width="962" height="572" alt="image" src="https://github.com/user-attachments/assets/ca6331bc-3aea-44c8-a097-4a7084169e76" />

💡 Recomendaciones por Género

La app incluye un comando para recomendar lecturas. Filtra los libros por género y devuelve los mejor puntuados.

Ejemplo de uso:
```python
python manage.py recomendar_por_genero aventura
```

Ejemplo de resultado:

<img width="973" height="273" alt="image" src="https://github.com/user-attachments/assets/cb24c910-6baa-4db1-b984-9ae041a305eb" />

Si el género no existe, se devuelve un aviso de error:

<img width="979" height="109" alt="image" src="https://github.com/user-attachments/assets/f281eb22-3a44-4ff8-946c-da0dafa792d9" />

Si el género existe, pero no hay libros calificados:

⚠️ No se encontraron libros en el género o no tienen calificaciones.

⚖️ Licencias

✅ Python → PSF License

✅ Django → BSD License

✅ PostgreSQL → PostgreSQL License

✅ Pandas → BSD License

✅ Matplotlib → PSF-based License

✅ Seaborn → BSD License

✅ Scikit-learn → BSD License

Este proyecto está cubierto por la licencia MIT. Consulta el archivo LICENSE para más detalles.
