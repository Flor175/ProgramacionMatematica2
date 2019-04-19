from django import forms
from Archivos.models import  Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ("archivo",)
       

#class EditarForm(forms.Form):
   # id_archivo = forms.HiddenInput()
   # texto = forms.TextInput()