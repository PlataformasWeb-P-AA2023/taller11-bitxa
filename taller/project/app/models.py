from django.db import models

class Edificio(models.Model):
    TIPO_CHOICES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
    ]
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
