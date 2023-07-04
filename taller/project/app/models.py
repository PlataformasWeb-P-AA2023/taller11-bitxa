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

    def __str__(self):
        return f'Nombre: {self.nombre} \n Direccion: {self.direccion} \n Ciudad: {self.ciudad} \n Tipo: {self.tipo}'

    
class Departamento(models.Model):

    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return f'Nombre Propietario: {self.nombre_propietario} \n Costo: {self.costo} \n Numero de Cuartos: {self.numero_cuartos} \n Edificio: {self.edificio.nombre}'
