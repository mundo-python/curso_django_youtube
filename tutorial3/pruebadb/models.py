from django.db import models

class Empresa(models.Model):
	nombre = models.CharField(max_length=20)
	fundacion = models.IntegerField()
	#empleados -> foreignKey -> programador

	def __str__(self):
		return self.nombre

class Lenguaje(models.Model):
	nombre = models.CharField(max_length=40)
	creador = models.CharField(max_length=40, null=True)

	def __str__(self):
		return self.nombre

class Programador(models.Model):
	nombre = models.CharField(max_length=40)
	edad = models.IntegerField(null=True)
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, 
											related_name="empleados")
	lenguaje = models.ManyToManyField(Lenguaje)

	def __str__(self):
		return self.nombre