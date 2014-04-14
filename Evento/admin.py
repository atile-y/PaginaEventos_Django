from django.contrib import admin

from Evento.models import GeneroMusical, TipoEvento, TipoObraTeatro, TipoDanza, Evento

# Register your models here.

admin.site.register(GeneroMusical)
admin.site.register(TipoEvento)
admin.site.register(TipoObraTeatro)
admin.site.register(TipoDanza)
admin.site.register(Evento)

