from django.db import models

# Create your models here.

class Precio(models.Model):
    precio = models.DecimalField(max_digits=7, decimal_places=2)

class Hora(models.Model):
    hora = models.TimeField()

class Fecha(models.Model):
    fecha = models.DateField()

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=50)

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    generosmusicales = models.ManyToManyField(GeneroMusical)

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=50)

class TipoObraTeatro(models.Model):
    nombre = models.CharField(max_length=50)

class TipoDanza(models.Model):
    nombre = models.CharField(max_length=50)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    URLImg = models.ImageField(upload_to='eventosImg/%Y/%m/%d')
    URLWeb = models.URLField()
    descripcion = models.TextField()
    fecHoraPub = models.DateTimeField(auto_now_add=True)
    nVisitas = models.IntegerField()
    precios = models.ManyToManyField(Precio)
    horas = models.ManyToManyField(Hora)
    fechas = models.ManyToManyField(Fecha)
    tipoevento = models.ForeignKey(TipoEvento)

class EventoConcierto(models.Model):
    idEventoConcierto = models.ForeignKey(Evento, primary_key=True)
    generomusical = models.ForeignKey(GeneroMusical)

class EventoObraTeatro(models.Model):
    idEventoObraTeatro = models.ForeignKey(Evento, primary_key=True)
    tipoobrateatro = models.ForeignKey(TipoObraTeatro)

class EventoDanza(models.Model):
    idEventoDanza = models.ForeignKey(Evento, primary_key=True)
    tipodanza = models.ForeignKey(TipoDanza)

