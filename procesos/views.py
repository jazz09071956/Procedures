from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
import procesos.models as models1
from procesos import forms as forms1
from .sweetalert_mixin import SweetAlertMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from io import BytesIO
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
import procesos.resources as resources1

# Create your views here.
"""
Procesos
"""
class ProcesoList(LoginRequiredMixin, ListView):
    model = models1.Proceso
    template_name = 'procesos/proceso_listado.html'
    context_object_name="procesos" # predeterminado es: object_list

class ProcesoDetail(LoginRequiredMixin, DetailView):
    model = models1.Proceso
    template_name = 'procesos/proceso_extendido.html'
    context_object_name="proceso"

class ProcesoCreate(SweetAlertMixin, LoginRequiredMixin, CreateView):
    model=models1.Proceso
    template_name="procesos/proceso_adicionar.html"
    context_object_name="proceso"
    form_class=forms1.ProcesoForm
    # el CreateView requiere un success_url
    success_url=reverse_lazy("proceso_listado")
    success_message = "Proceso adicionado con Exito!"
    
class ProcesoUpdate(SweetAlertMixin, LoginRequiredMixin, UpdateView):
    model=models1.Proceso
    template_name="procesos/proceso_editar.html"
    form_class=forms1.ProcesoEditForm
    # el CreateView requiere un success_url
    success_url=reverse_lazy("proceso_listado")
    success_message="Proceso Actualizado Exitosamente"
    context_object_name="proceso"
    

class ProcesoDelete(SweetAlertMixin, LoginRequiredMixin, DeleteView):
    model = models1.Proceso
    template_name = 'procesos/proceso_eliminar.html'
    success_url = reverse_lazy('proceso_listado')
    context_object_name="proceso"
    success_message="Proceso Eliminado Exitosamente"


"""
Detalle de Procesos
"""

class Detalle_ProcesoList(LoginRequiredMixin, ListView):
    model = models1.Detalle_Proceso
    template_name = 'procesos/detalle_proceso_listado.html'
    context_object_name="detalles_proceso" # predeterminado es: object_list

    def get_queryset(self):
        # Filtrar the child records based on the parent's key
        parent_pk = self.kwargs['parent_pk']
        #return models1.Detalle_Proceso.objects.filter(proceso_id=parent_pk)
        #return models1.Detalle_Proceso.objects.filter(parent__pk=parent_pk)
        return models1.Detalle_Proceso.objects.filter(proceso__pk=parent_pk).order_by('correlativo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pasar variables de contexto al templete
        parent_pk= self.kwargs['parent_pk']
        parent=models1.Proceso.objects.get(pk=parent_pk)
        context['parent_pk'] = parent_pk
        context['parent_name'] = parent.nombre_proceso
        return context


class Detalle_ProcesoDetail(LoginRequiredMixin, DetailView):
    model = models1.Detalle_Proceso
    template_name = 'procesos/detalle_proceso_extendido.html'
    context_object_name="detalle_proceso"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        parent_pk= self.kwargs['parent_pk']
        parent=models1.Proceso.objects.get(pk=parent_pk)
        context['parent_pk'] = parent_pk
        context['parent_name'] = parent.nombre_proceso
        #

        return context

class Detalle_ProcesoCreate(SweetAlertMixin, LoginRequiredMixin, CreateView):
    model=models1.Detalle_Proceso
    template_name="procesos/detalle_proceso_adicionar.html"
    context_object_name="detalle_proceso"
    form_class=forms1.Detalle_ProcesoForm
    # el CreateView requiere un success_url
    success_url=reverse_lazy("detalle_proceso_listado")
    success_message = "Detalle de Proceso adicionado con Exito!"

    def form_valid(self, form):
        form.instance.proceso_id = self.kwargs['parent_pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_pk= self.kwargs['parent_pk']
        parent=models1.Proceso.objects.get(pk=parent_pk)
        #context['parent_pk'] = self.kwargs['parent_pk']  # Pass the parent's key to the template
        context['parent_pk'] = parent_pk
        context['parent_name'] = parent.nombre_proceso
        return context

    # para formar bien la URL
    def get_success_url(self):
        return reverse('detalle_proceso_listado', kwargs={'parent_pk': self.kwargs['parent_pk']}) 

class Detalle_ProcesoUpdate(SweetAlertMixin, LoginRequiredMixin, UpdateView):
    model=models1.Detalle_Proceso
    template_name="procesos/detalle_proceso_editar.html"
    form_class=forms1.Detalle_ProcesoEditForm
    # el CreateView requiere un success_url
    success_url=reverse_lazy("detalle_proceso_listado")
    success_message="Detalle de Proceso Actualizado Exitosamente"
    context_object_name="detalle_proceso"

    def form_valid(self, form):
        form.instance.proceso_id = self.kwargs['parent_pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the current instance to the context to access it in the template
        context['instance'] = self.object
        #
        parent_pk= self.kwargs['parent_pk']
        parent=models1.Proceso.objects.get(pk=parent_pk)
        #context['parent_pk'] = self.kwargs['parent_pk']  # Pass the parent's key to the template
        context['parent_pk'] = parent_pk
        context['parent_name'] = parent.nombre_proceso
        return context
    

    def get_success_url(self):
        #return reverse('detalle_proceso_extendido', kwargs={'parent_pk': self.kwargs['parent_pk'], 'pk': #self.kwargs['pk']})
        return reverse('detalle_proceso_listado', kwargs={'parent_pk': self.kwargs['parent_pk']})
    
class Detalle_ProcesoDelete(SweetAlertMixin, LoginRequiredMixin, DeleteView):
    model = models1.Detalle_Proceso
    template_name = 'procesos/detalle_proceso_eliminar.html'
    success_url = reverse_lazy('detalle_proceso_listado')
    context_object_name="detalle_proceso"
    success_message="Detalle de Proceso Eliminado Exitosamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_pk= self.kwargs['parent_pk']
        parent=models1.Proceso.objects.get(pk=parent_pk)
        #context['parent_pk'] = self.kwargs['parent_pk']  # Pass the parent's key to the template
        context['parent_pk'] = parent_pk
        context['parent_name'] = parent.nombre_proceso
        return context

    def get_success_url(self):
        return reverse('detalle_proceso_listado', kwargs={'parent_pk': self.kwargs['parent_pk']})
