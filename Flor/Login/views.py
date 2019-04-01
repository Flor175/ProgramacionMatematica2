from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import RegistroForm, NuevoRegistro, Inicio_sesion, DocumentoForm
from .models import Usuario, Documento
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html')


@transaction.atomic
def registro(request):
    if request.method == 'POST':
        form1 = RegistroForm(request.POST)
        form2 = NuevoRegistro(request.POST)
        if form1.is_valid() and form2.is_valid():
            nuevo_usuario = form1.save()
            nuevo_usuario.refresh_from_db()
            extra_usuario = NuevoRegistro(request.POST, instance=nuevo_usuario.usuario)
            extra_usuario.full_clean()
            extra_usuario.save()
            return redirect('home')
    else:
        form1 = RegistroForm()
        form2 = NuevoRegistro()
    return render(request, 'signup.html', {'formulario1': form1, "formulario2":form2}) 

def inicio(request):
    if request.method == "POST":
        form = Inicio_sesion(request.POST or None)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get("nombre")
            contras = datos.get("passw")
            inicio = authenticate(username=nombre, password=contras)
            if inicio is not None:
                login(request, inicio)
                return redirect('home')
            else:
                return redirect('inicio')
    else:
        form = Inicio_sesion()   
    return render(request, "login.html", {"formulario":form})   

def subida_archivos(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentoForm()
    return render(request, 'subida_archivos.html', {
        'form': form
    })

def archivos_subidos(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_doc = Documento(docfile=request.FILES['docfile'])
            nuevo_doc.save()
            return redirect(reverse('archivos_subidos'))

    else:
        form = DocumentoForm()

    documentos = Documento.objects.all()
    return render(request, 'archivos_subidos.html', {'documentos': documentos, 'form': form})