from django.db import models

from uuid import uuid4
from time import strftime
import os.path

# Create your models here.

def imageName(instance, filename):
    if instance.id:
        est = Establecimiento.objects.get(pk=instance.id)
        os.remove(est.URLImg.path)
    path = 'establecimientosImg/' + strftime('%Y/%m/%d/') + str(uuid4())
    path += os.path.splitext(filename)[1]
    return path

class TipoComida(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

class TipoRestaurante(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

class TipoEscuela(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre

class TipoEstablecimiento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return unicode(self.nombre)

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    URLImg = models.ImageField(upload_to=imageName, verbose_name='imagen')
    URLWeb = models.URLField('pagina web')
    descripcion = models.TextField()
    calle = models.CharField(max_length=50)
    noInt = models.CharField(max_length=10,
                verbose_name='numero interior')
    noExt = models.CharField(max_length=10,
                verbose_name='numero exterior')
    colonia = models.CharField(max_length=50)
    delegacion = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    CP = models.IntegerField('codigo postal')
    fecHoraPub = models.DateTimeField(auto_now_add=True)
    nVisitas = models.IntegerField(default=0, editable=False)
    tipoestablecimiento = models.ForeignKey(TipoEstablecimiento)

    def __unicode__(self):
        return unicode(self.nombre)

class EstablecimientoRestaurante(models.Model):
    idEstablecimientoRestaurante = models.ForeignKey(Establecimiento,
            primary_key=True)
    tipocomida = models.ForeignKey(TipoComida)
    tiporestaurante = models.ForeignKey(TipoRestaurante)

class EstablecimientoBar(models.Model):
    idEstablecimientoBar = models.ForeignKey(Establecimiento,
            primary_key = True)
    karaoke = models.BooleanField(default=False)
    baile = models.BooleanField(default=False)
    mariachis = models.BooleanField(default=False)
    generosmusicales = models.ManyToManyField('Evento.GeneroMusical')

class EstablecimientoEscuela(models.Model):
    idEstablecimientoEscuela = models.ForeignKey(Establecimiento,
            primary_key=True)
    tipoescuela = models.ForeignKey(TipoEscuela)

