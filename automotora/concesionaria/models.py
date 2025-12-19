from django.db import models


class Automotora(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email_contacto = models.EmailField()

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Auto(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50) 
    anio = models.IntegerField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"