from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from PaginaEventos import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^evento/', include('Evento.urls', namespace="Evento")),
    url(r'^establecimiento/', include('Establecimiento.urls',
                                      namespace="Establecimiento")),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

