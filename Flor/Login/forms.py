from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Documento

class RegistroForm(UserCreationForm):
    username = forms.CharField(help_text="Obligatorio. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.", label="Nombre de Usuario")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text="La contraseña no debe contener más de 8 caractéres", label="Contraseña")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2" )
        labels = {
            "username": ("Nombre de Usuario"),
            "password1": ("Contraseña"),
            
        }
        help_texts = {
            "password1": "La contraseña no debe contener más de 8 caractéres",
            "password2": "Escriba su contraseña de nuevo",
        }
        error_messages = {
            "username": {
                "max_length": ("El nombre de usuario es muy largo"),
                "min_length": ("El nombre de usuario es muy corto"),
                "unique": ("Este nombre ya fue utilizado")
            },
            "email": {
                "invalid": ("Correo inválido"),
            },
        }

class NuevoRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("numero_carnet", "cui", "profesion")
        labels = {
            "numero_carnet": ("Número de Carnet"),
            "profesion": ("Profesión"),
        }

class Inicio_sesion(forms.Form):
    nombre = forms.CharField(max_length=150, required=True, label="Nombre de Usuario")
    passw = forms.CharField(max_length=150, required=True, label="Contraseña", widget=forms.PasswordInput())

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ("archivo",)