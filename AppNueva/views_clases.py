from django.shortcuts import render
from .models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CursoListView(LoginRequiredMixin, ListView):
     model = Curso
     template_name = "AppNueva/Vistas_Clases/curso_lista.html"


class CursoDetalle(LoginRequiredMixin, DetailView):
     model = Curso
     template_name = "AppNueva/Vistas_Clases/curso_detalle.html"


class CursoCreateView(LoginRequiredMixin, CreateView):
     model = Curso
     template_name = "AppNueva/Vistas_Clases/curso_formulario.html"
     success_url = reverse_lazy("Lista")
     fields = ["nombre", "comision"]


class CursoUpdateView(LoginRequiredMixin, UpdateView):
     model = Curso
     template_name = "AppNueva/Vistas_Clases/curso_editar.html"
     #success_url = reverse_lazy("List")
     success_url = "/AppNueva/clases/lista/"
     fields = ["nombre", "comision"]


class CursoDeleteView(DeleteView):
     model = Curso
     success_url = reverse_lazy("Lista")
     template_name = "AppNueva/Vistas_Clases/curso_confirm_delete.html"