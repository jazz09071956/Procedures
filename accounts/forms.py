from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__" 