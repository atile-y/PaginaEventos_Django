from django.views import generic
from django.utils import timezone

from Evento.models import Evento

class HomeView(generic.ListView):
    template_name = 'PaginaEventos/home.html'
    context_object_name = 'eve_filter'

    def get_queryset(self):
        """
        Regresa los primeros 4 eventos publicados (sin incluir a los que
        seran publicados en el futuro).
        """
        return Evento.objects.filter(
            fecHoraPub__lte=timezone.now()
        ).order_by('-fecHoraPub')[:4]

