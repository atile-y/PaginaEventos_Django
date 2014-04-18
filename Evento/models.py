from django.db import models

# Create your models here.

class Precio(models.Model):
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return unicode(self.precio)

class Hora(models.Model):
    hora = models.TimeField()

    def __unicode__(self):
        return unicode(self.hora)

class Fecha(models.Model):
    fecha = models.DateField()

    def __unicode__(self):
        return unicode(self.fecha)

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    generosmusicales = models.ManyToManyField(GeneroMusical,
            verbose_name='genero musical')

    def __unicode__(self):
        return unicode(self.nombre)

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class TipoObraTeatro(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class TipoDanza(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    URLImg = models.ImageField(upload_to='eventosImg/%Y/%m/%d',
            verbose_name='imagen')
    URLWeb = models.URLField('pagina web')
    descripcion = models.TextField()
    fecHoraPub = models.DateTimeField(auto_now_add=True)
    nVisitas = models.IntegerField(default=0, editable=False)
    precios = models.ManyToManyField(Precio)
    horas = models.ManyToManyField(Hora)
    fechas = models.ManyToManyField(Fecha)
    tipoevento = models.ForeignKey(TipoEvento)
    artistas = models.ManyToManyField(Artista)

    def __unicode__(self):
        return self.nombre

class EventoConcierto(models.Model):
    idEventoConcierto = models.ForeignKey(Evento, primary_key=True)
    generomusical = models.ForeignKey(GeneroMusical)

class EventoObraTeatro(models.Model):
    idEventoObraTeatro = models.ForeignKey(Evento, primary_key=True)
    tipoobrateatro = models.ForeignKey(TipoObraTeatro)

class EventoDanza(models.Model):
    idEventoDanza = models.ForeignKey(Evento, primary_key=True)
    tipodanza = models.ForeignKey(TipoDanza)

