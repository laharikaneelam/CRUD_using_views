from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from app.models import student,school
from django.urls import reverse_lazy
# Create your views here.

class templateViewClass(TemplateView):
    template_name="app/index.html"

class listViewClass(ListView):
    model=school

class detailViewClass(DetailView):
    model=school

class createViewClass(CreateView):
    model=school
    fields=('name','principal','location')

class updateViewClass(UpdateView):
    model=school
    fields=('principal',)

class deleteViewClass(DeleteView):
    model=school
    success_url=reverse_lazy('list')
