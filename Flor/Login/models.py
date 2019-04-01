from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validate_file_extension
# Create your models here.

class Usuario(models.Model):
    MATEMATICA = "1"
    FISICA = "2"
    Carreras = (
        (MATEMATICA, "Matemática"),
        (FISICA, "Física")
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_carnet = models.CharField(max_length=9, blank=True, null=True, unique=True)
    cui = models.CharField(max_length=13, blank=True, null=True, unique=True)
    profesion = models.CharField(max_length=100, choices=Carreras, default=MATEMATICA)

    objects = models.Manager()

    def __str__(self):
        return self.usuario.username 

@receiver(post_save, sender = User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
    instance.usuario.save()

class Documento(models.Model):
    archivo = models.FileField(upload_to='Documentos/', validators=[validate_file_extension])



    