
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('libros.urls')),
    path('api/', include('cuentas.urls'))
]
