from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'
    context_object_name = 'snack'

class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snack_create.html'
    fields = '__all__'

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snack_update.html'
    fields = '__all__'
    success_url = reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snack_delete.html'
    success_url = reverse_lazy('snack_list')
