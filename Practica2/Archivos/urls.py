from django.contrib import admin
from django.urls import path
from Archivos.views import subida_archivos, ver_archivo, lista_archivos, analizar_archivo, guardar, ArchivosView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('subida_archivos/', subida_archivos, name='subida_archivos'),
    path('archivos_subidos/', lista_archivos, name='archivos_subidos'),
    path('lectura/', ver_archivo, name='leer'),
    path('editar/', guardar, name='guardar' ),
    path('analizar/', analizar_archivo, name='analizar' ),
    path('archivos/', ArchivosView.as_view(), name='archivos'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)