from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    PONENCIA = 'PO'
    RECREATIVO = 'RE'
    TGLOBAL = 'GO'
    CONVERSATORIO = 'CO'
    OTRO = 'OT'
    TIPO_CHOICES = [
        (PONENCIA, 'Ponencia'),
        (RECREATIVO, 'Recreativo'),
        (TGLOBAL, 'Global'),
        (CONVERSATORIO, 'Convesatorio'),
        (OTRO, 'Otro'),
    ]
    nombre = models.CharField('Evento', max_length=60)
    fecha = models.DateField('Fecha')
    lugar = models.CharField('Lugar', max_length=60)
    tipo = models.CharField('Tipo', max_length=15, choices=TIPO_CHOICES)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['-nombre']

class Ponente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.PositiveIntegerField('Cedula')
    email = models.EmailField('Correo')
    telefono = models.PositiveIntegerField('Telefono', blank=True)
    website = models.URLField('Sitio Web', blank=True)
    eventos = models.ManyToManyField(Evento, blank=True)
    def __str__(self):
        return "%s's profile" % self.user

class Ponencia(models.Model):
    nombre = models.CharField('Ponencia', max_length=45)
    ponente = models.ForeignKey(Ponente)
    descripcion = models.TextField('Descripcion', max_length=200)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Asistente(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    cedula = models.PositiveIntegerField('Cedula', primary_key=True)
    email = models.EmailField('Correo')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.nombre

class Patrocinador(models.Model):
    MONETARIO = 'MO'
    APOYO = 'AP'
    PUBLICIDAD = 'PU'
    PARTICIPANTE = 'PA'
    ORGANIZATIVO = 'OR'
    MODO_CHOICES = [
        (MONETARIO, 'Monetario'),
        (APOYO, 'Apoyo'),
        (PUBLICIDAD, 'Publicidad'),
        (PARTICIPANTE, 'Participante'),
        (ORGANIZATIVO, 'Organizativo'),
    ]
    nombre = models.CharField('Nombre', max_length=60)
    cedula = models.IntegerField('Cedula o Rif')
    gerente = models.CharField('Encargado', max_length=50)
    sitioWeb = models.URLField('Sitio Web')
    direccion = models.TextField('Direccion', max_length=150)
    telefono = models.PositiveIntegerField('Telefono')
    modalidad = models.CharField('Modalidad de Patrocinio', max_length=15, choices=MODO_CHOICES)
    eventos = models.ManyToManyField(Evento)
    def __str__(self):
        return self.nombre