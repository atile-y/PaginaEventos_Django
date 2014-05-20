# from django.shortcuts import render, get_object_or_404
from django.views import generic

from Establecimiento.models import Establecimiento

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Establecimiento/index.html'
    context_object_name = 'est_list'

    def get_queryset(self):
        """Regresa los establecimientos publicados."""
        return Establecimiento.objects.order_by('-nombre')

class DetailView(generic.DetailView):
    model = Establecimiento
    template_name = 'Establecimiento/detail.html'

