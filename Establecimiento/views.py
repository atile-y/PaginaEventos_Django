from django.shortcuts import render, get_object_or_404

from Establecimiento.models import Establecimiento

# Create your views here.

def index(request):
    est_list = Establecimiento.objects.all().order_by('-nombre')
    context = {'est_list': est_list}
    return render(request, 'Establecimiento/index.html', context)

def detail(request, est_id):
    est = get_object_or_404(Establecimiento, pk=est_id)
    return render(request, 'Establecimiento/detail.html', {'est': est})

