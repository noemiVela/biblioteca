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

<img width="676" height="410" alt="image" src="https://github.com/user-attachments/assets/7b629973-55d5-4543-8e24-61856d550516" />

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

<img width="672" height="378" alt="image" src="https://github.com/user-attachments/assets/011aea05-fe39-424f-bbd0-1c610be16f73" />

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

<img width="502" height="392" alt="image" src="https://github.com/user-attachments/assets/0bba0c08-7ea0-4962-853b-b4dd0d5b31e0" />

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

<img width="500" height="317" alt="image" src="https://github.com/user-attachments/assets/389818ff-235e-479f-8421-7bc4da472c83" />

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

<img width="504" height="303" alt="image" src="https://github.com/user-attachments/assets/a63fd766-5eb6-49f9-ace6-f3a5ebeaa4e2" />

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

<img width="509" height="432" alt="image" src="https://github.com/user-attachments/assets/0f89462f-6369-4993-bbc3-0b47f0d2d3bd" />

Promedio de calificación por usuario:

<img width="533" height="422" alt="image" src="https://github.com/user-attachments/assets/11a9d5f0-8405-4990-9e80-9ecdae6f2807" />

Cantidad de libros en cada género:

<img width="538" height="394" alt="image" src="https://github.com/user-attachments/assets/447b5c7e-c4b8-4fc3-8e22-b728d951f90d" />

Libros con mejor promedio de calificación

<img width="1244" height="616" alt="image" src="https://github.com/user-attachments/assets/0fa7e826-9c32-413d-a3ec-4d9181b6b291" />

Media de valoración por género

<img width="977" height="579" alt="image" src="https://github.com/user-attachments/assets/ebc9f82a-c636-41a5-840c-3869c915ee24" />

Libros más valorados

<img width="977" height="581" alt="image" src="https://github.com/user-attachments/assets/ba7c1ecb-0d5f-4fb1-bd47-19ab437d40db" />

Autores con más calificaciones

<img width="985" height="580" alt="image" src="https://github.com/user-attachments/assets/08864ecb-2e47-4f18-ab39-b68a5c50e159" />

Evolución de publicaciones a lo largo de los años

<img width="982" height="576" alt="image" src="https://github.com/user-attachments/assets/2e807dc1-3600-491f-b3b7-444488d5239d" />

💡 Recomendaciones por Género

La app incluye un comando para recomendar lecturas. Filtra los libros por género y devuelve los mejor puntuados.

Ejemplo de uso:
```python
python manage.py recomendar_por_genero aventura
```

Ejemplo de resultado:

<img width="743" height="293" alt="image" src="https://github.com/user-attachments/assets/053de4c6-5eb3-4d1c-a8ab-583183ea78c0" />

Si el género no existe, se devuelve un aviso de error:

<img width="745" height="113" alt="image" src="https://github.com/user-attachments/assets/af504c0e-6cd8-4f4a-9812-44782caa7e36" />

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
