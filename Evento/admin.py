from django import forms
from django.contrib import admin

from Evento.models import Evento, Artista
from Evento.models import Precio, Fecha, Hora

# Register your models here.

class PrecioInline(admin.TabularInline):
    model = Evento.precios.through
    extra = 1

class FechaInline(admin.TabularInline):
    model = Evento.fechas.through
    extra = 1

class HoraInline(admin.TabularInline):
    model = Evento.horas.through
    extra = 1

class ArtistaInline(admin.TabularInline):
    model = Evento.artistas.through
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    inlines = [PrecioInline, HoraInline, FechaInline, ArtistaInline,]
    exclude = ('precios', 'horas', 'fechas', 'artistas',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Artista)
admin.site.register(Precio)
admin.site.register(Fecha)
admin.site.register(Hora)

