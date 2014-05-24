from django.views import generic
from django.utils import timezone

from Evento.models import Evento

class HomeView(generic.ListView):
    template_name = 'PaginaEventos/home.html'
    context_object_name = 'eve_filter'

    def get_queryset(self):
        """
        Regresa los proximos 8 eventos (sin incluir a los que
        ya ocurrieron).
        """
        eventos = Evento.objects.exclude(
                        fechas__fecha__lt=timezone.now()
                    ).order_by(
                        'fechas__fecha', 'nombre'
                    )[:8]
        nombres = set()
        unicos = []
        for item in eventos:
            if item.nombre not in nombres:
                unicos.append(item)
                nombres.add(item.nombre)
        return unicos

