from django.db import models
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from libros.models import Libro, Autor, Genero, Calificacion
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class Command(BaseCommand):
    help = 'Genera 10 reportes gráficos basados en los modelos de la biblioteca'

    def handle(self, *args, **kwargs):
        output_dir = "reporte_graficos"
        os.makedirs(output_dir, exist_ok=True)

        def save_plot(fig, filename):
            path = os.path.join(output_dir, filename)
            fig.savefig(path, bbox_inches='tight')
            plt.close(fig)

        # Usar un tema diferente en Seaborn
        sns.set_theme(style="whitegrid", palette="pastel")

        # ===============================
        # 1. Libros por género (Pie Chart)
        df1 = pd.DataFrame(
            list(Genero.objects.annotate(cantidad=models.Count('libros')).values('nombre', 'cantidad'))
        )

        if not df1.empty:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(
                df1['cantidad'],
                labels=df1['nombre'],
                autopct='%1.1f%%',
                startangle=140,
                colors=sns.color_palette("pastel")
            )
            ax.set_title('Distribución de Libros por Género', fontsize=14)
            save_plot(fig, "1_libros_por_genero.png")

        # ===============================
        # 2. Libros por autor (Horizontal Barplot, rocket palette)
        df2 = pd.DataFrame(
            list(Autor.objects.annotate(cantidad=models.Count('libros')).values('nombre', 'cantidad'))
        )
        df2 = df2.sort_values(by='cantidad', ascending=True).head(10)
        if not df2.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df2, y='nombre', x='cantidad', ax=ax, palette='rocket')
            ax.set_title('Top 10 Autores con Más Libros', fontsize=14)
            ax.set_xlabel('Cantidad de Libros')
            ax.set_ylabel('Autor')
            for p in ax.patches:
                ax.annotate(f'{int(p.get_width())}',
                            (p.get_width(), p.get_y() + p.get_height()/2),
                            ha='left', va='center', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "2_libros_por_autor.png")

        # ===============================
        # 3. Promedio de calificación por libro (barplot, crest palette)
        df3 = pd.DataFrame(
            list(Libro.objects.annotate(prom=models.Avg('calificaciones__calificacion'))
                 .values('titulo', 'prom'))
        )
        df3 = df3.dropna().sort_values(by='prom', ascending=False).head(10)

        if not df3.empty:
            fig, ax = plt.subplots(figsize=(16, 8))
            sns.barplot(data=df3, x='titulo', y='prom', ax=ax, palette='crest')
            ax.set_title('Promedio de Calificación por Libro', fontsize=16)
            ax.set_xlabel('Título', fontsize=12)
            ax.set_ylabel('Promedio de Calificación', fontsize=12)
            plt.xticks(rotation=45, ha='right')
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.1f}',
                            (p.get_x() + p.get_width()/2., p.get_height() + 0.05),
                            ha='center', va='bottom', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "3_promedio_calificacion_libro.png")

        # ===============================
        # 4. Promedio de calificación por género (horizontal barplot)
        df4 = pd.DataFrame(
            list(
                Genero.objects.annotate(prom=models.Avg('libros__calificaciones__calificacion'))
                .values('nombre', 'prom')
            )
        )
        df4 = df4.dropna()

        if not df4.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df4, y='nombre', x='prom', ax=ax, palette='magma')
            ax.set_title('Valoración Media según Género Literario', fontsize=14)
            ax.set_xlabel('Promedio de Calificación')
            ax.set_ylabel('Género')
            for p in ax.patches:
                ax.annotate(f'{p.get_width():.1f}',
                            (p.get_width(), p.get_y() + p.get_height()/2),
                            ha='left', va='center', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "4_promedio_calificacion_genero.png")

        # ===============================
        # 5. Calificaciones por usuario (vertical barplot)
        df5 = pd.DataFrame(
            list(
                User.objects.annotate(cantidad=models.Count('calificaciones'))
                .values('username', 'cantidad')
            )
        )
        df5 = df5[df5['cantidad'] > 0]

        if not df5.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df5, x='username', y='cantidad', ax=ax, palette='viridis')
            ax.set_title('Cantidad de Calificaciones por Usuario', fontsize=14)
            ax.set_xlabel('Usuario')
            ax.set_ylabel('Cantidad de Calificaciones')
            plt.xticks(rotation=45, ha='right')
            for p in ax.patches:
                ax.annotate(f'{int(p.get_height())}',
                            (p.get_x() + p.get_width()/2., p.get_height() + 0.1),
                            ha='center', va='bottom', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "5_calificaciones_por_usuario.png")

        # ===============================
        # 6. Libros con más calificaciones (horizontal barplot)
        df6 = pd.DataFrame(
            list(
                Libro.objects.annotate(cantidad=models.Count('calificaciones'))
                .values('titulo', 'cantidad')
            )
        )
        df6 = df6[df6['cantidad'] > 0].sort_values(by='cantidad', ascending=True).head(10)

        if not df6.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df6, y='titulo', x='cantidad', ax=ax, palette='cubehelix')
            ax.set_title('Libros con Más Calificaciones', fontsize=14)
            ax.set_xlabel('Cantidad de Calificaciones')
            ax.set_ylabel('Título del Libro')
            for p in ax.patches:
                ax.annotate(f'{int(p.get_width())}',
                            (p.get_width(), p.get_y() + p.get_height()/2),
                            ha='left', va='center', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "6_libros_mas_calificados.png")

        # ===============================
        # 7. Autores con más libros calificados
        df7 = pd.DataFrame(
            list(
                Autor.objects.annotate(total=models.Count('libros__calificaciones'))
                .values('nombre', 'total')
            )
        )
        df7 = df7[df7['total'] > 0].sort_values(by='total', ascending=False).head(10)

        if not df7.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df7, x='nombre', y='total', ax=ax, palette='flare')
            ax.set_title('Autores con Más Libros Calificados', fontsize=14)
            ax.set_xlabel('Autor')
            ax.set_ylabel('Total de Calificaciones')
            plt.xticks(rotation=45, ha='right')
            for p in ax.patches:
                ax.annotate(f'{int(p.get_height())}',
                            (p.get_x() + p.get_width()/2., p.get_height() + 0.1),
                            ha='center', va='bottom', fontsize=9)
            fig.tight_layout()
            save_plot(fig, "7_autores_mas_calificados.png")

        # ===============================
        # 8. Libros publicados por año (Área plot)
        df8 = pd.DataFrame(list(Libro.objects.values('fecha_publicacion')))
        if not df8.empty:
            df8['anio'] = pd.to_datetime(df8['fecha_publicacion']).dt.year
            df8 = df8.groupby('anio').size().reset_index(name='cantidad')
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.fill_between(df8['anio'], df8['cantidad'], color='coral', alpha=0.5)
            ax.plot(df8['anio'], df8['cantidad'], color='coral')
            ax.set_title('Libros Publicados por Año')
            ax.set_xlabel('Año')
            ax.set_ylabel('Cantidad')
            fig.tight_layout()
            save_plot(fig, "8_publicaciones_por_anio.png")

        # ===============================
        # 9. Histograma de calificaciones (kdeplot)
        df9 = pd.DataFrame(list(Calificacion.objects.values('calificacion')))
        if not df9.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.kdeplot(df9['calificacion'], fill=True, color="purple", alpha=0.6, ax=ax)
            ax.set_title('Distribución de Calificaciones', fontsize=14)
            ax.set_xlabel('Calificación')
            ax.set_ylabel('Densidad')
            fig.tight_layout()
            save_plot(fig, "9_histograma_calificaciones.png")

        # ===============================
        # 10. Promedio de calificación por usuario (scatter plot)
        df10 = pd.DataFrame(
            list(
                User.objects.annotate(prom=models.Avg('calificaciones__calificacion'))
                .values('username', 'prom')
            )
        )
        df10 = df10.dropna()

        if not df10.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(data=df10, x='username', y='prom', color='green', s=100, ax=ax)
            ax.set_title('Promedio de Calificación por Usuario', fontsize=14)
            ax.set_xlabel('Usuario')
            ax.set_ylabel('Promedio')
            plt.xticks(rotation=45, ha='right')
            fig.tight_layout()
            save_plot(fig, "10_promedio_usuario.png")

        self.stdout.write(self.style.SUCCESS(f"✅ Reportes generados en la carpeta '{output_dir}'"))
