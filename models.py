from django.db import models
import datetime

class Usuario(models.Model):
    nombre = models.CharField(blank=False, null = False, max_length=50)
    ap_paterno = models.CharField(blank=False, null = False, max_length=50)
    ap_materno = models.CharField(blank=False, null = False, max_length=50)
    direccion = models.CharField(blank=False, null = False, max_length=50)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.EmailField(blank=True, null = True, max_length=50)
    fecha_nacimiento = models.DateField(default=datetime.datetime.today)
    contrasena = models.CharField(blank=False, null = False, max_length=50)
    foto = models.ImageField(blank=True)
    tipo = models.CharField(blank=False, null = False, max_length=50)

    def __str__(self):
        return self.nombre
