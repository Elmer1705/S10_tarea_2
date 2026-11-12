from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    pais_origen = models.CharField("País de origen", max_length=60, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="productos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.marca})"