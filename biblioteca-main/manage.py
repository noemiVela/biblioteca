#!/usr/bin/env python

"""
Script de gestión para el proyecto Django Biblioteca.
Permite correr comandos administrativos como runserver, migrate, etc.
"""

import sys
import os


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        message = (
            f"No se pudo importar Django. "
            f"¿Está instalado y disponible en tu variable PYTHONPATH? "
            f"¿Olvidaste activar el entorno virtual?"
        )
        raise ImportError(message) from error

    # Mensaje opcional antes de ejecutar
    # print("Ejecutando comando Django...")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Error ejecutando manage.py: {ex}")
        sys.exit(1)
