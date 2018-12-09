from django.db import models
from app_adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
       return '{}' .format(self.nombre )

class Mascota(models.Model):
    folio=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    sexo=models.CharField(max_length=10)
    edad_aproximada=models.IntegerField()
    fecha_rescate=models.DateField()
    persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
    vacuna=models.ManyToManyField(Vacuna)

    def __str__(self):
       return '{}' .format(self.nombre )


    #'{}' y un self.nombre      te regresara el nombre de la persona

    #tienes que hacer esto donde haya campos que te regresen un id en vez de nombre

#utilizar commandos makemigrations y migrate.



