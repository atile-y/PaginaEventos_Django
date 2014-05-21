from django.views import generic
from django.utils import timezone

from Evento.models import Evento

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Evento/index.html'
    context_object_name = 'eve_list'

    def get_queryset(self):
        """
        Regresa los eventos publicados por fecha mas proxima,
        despues por nombre, ignorando los que ya ocurrieron.
        """
        return Evento.objects.filter(
                    fechas__fecha__gte=timezone.now()
                ).order_by(
                    '-fechas__fecha', 'nombre'
                )

class DetailView(generic.DetailView):
    model = Evento
    template_name = 'Evento/detail.html'

