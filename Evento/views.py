from django.views import generic

from Evento.models import Evento

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Evento/index.html'
    context_object_name = 'eve_list'

    def get_queryset(self):
        """Regresa los eventos publicados."""
        return Evento.objects.order_by('-nombre')

class DetailView(generic.DetailView):
    model = Evento
    template_name = 'Evento/detail.html'

