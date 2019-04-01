"""Flor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Login import views as login_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_views.home, name = 'home'),
    path('registro/', login_views.registro, name='registro'),
    path('login/', login_views.inicio, name='inicio'),
    path('', login_views.inicio, name='inicio'),
    path('logout', login_views.inicio, name='logout'),
    path('subida_archivos/',login_views.subida_archivos, name='subida_archivos' ),
    path('archivos_subidos/', login_views.archivos_subidos, name= 'archivos_subidos')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
