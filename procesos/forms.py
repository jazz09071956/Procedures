from django import forms
from django.http import request
import procesos.models as models1

class ProcesoForm(forms.ModelForm):
  class Meta:
    model=models1.Proceso
    fields = ['id', 'codigo_proceso', 'nombre_proceso', 'descripcion_proceso']
    widgets = {
      'id': forms.TextInput(attrs={'readonly':'readonly'}),
    }
  #como se renderiza con bootstrap hay que sobreescribir el metodo init
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })

class ProcesoEditForm(forms.ModelForm):
  class Meta:
    model=models1.Proceso
    fields = ['id','codigo_proceso', 'nombre_proceso', 'descripcion_proceso', 'activo']
    widgets = {
      'id': forms.TextInput(attrs={'readonly':'readonly'}),
    }
  #como se renderiza con bootstrap hay que sobreescribir el metodo init
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })


class Detalle_ProcesoForm(forms.ModelForm):
  class Meta:
    model=models1.Detalle_Proceso
    fields = ['id','correlativo','nombre_detalle_proceso','descripcion_detalle_proceso', 'imagen']
    widgets = {
      'id': forms.TextInput(attrs={'readonly':'readonly'}),
    }
  #como se renderiza con bootstrap hay que sobreescribir el metodo init

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })

class Detalle_ProcesoEditForm(forms.ModelForm):
  class Meta:
    model=models1.Detalle_Proceso
    fields = ['id','correlativo','nombre_detalle_proceso','descripcion_detalle_proceso', 'imagen','activo']
    widgets = {
      'id': forms.TextInput(attrs={'readonly':'readonly'}),
    }
  #como se renderiza con bootstrap hay que sobreescribir el metodo init

  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class':'form-control'
      })
