from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import App
from .forms import AppForm

class AppListView(ListView):
    template_name = 'app/app_list.html'
    model = App
    paginate_by = 5

class AppDetailView(DetailView):
    template_name = 'app/app_detail.html'
    model = App

class AppCreateView(CreateView):
    template_name = 'app/app_create.html'
    model = App
    form_class = AppForm
    success_url = reverse_lazy('app:list')

class AppUpdateView(UpdateView):
    template_name = 'app/app_update.html'
    model = App
    form_class = AppForm
    success_url = reverse_lazy('app:list')

class AppDeleteView(DeleteView):
    template_name = 'app/app_confirm_delete.html'
    model = App
    success_url = reverse_lazy('app:list')



