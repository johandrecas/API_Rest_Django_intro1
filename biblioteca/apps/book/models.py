from django.db import models

# Create your models here.
class Author2(models.Model):
    nombre = models.CharField('Nombre',max_length=200,null=False,blank=False)
    apellido = models.CharField('Apellido',max_length=34)
    nacionalidad = models.CharField('Nacionalidad',max_length=45)
    estado = models.BooleanField(default=True)
    descripcion = models.TextField()
    fecha_de_creacion = models.DateField('Fecha Creacion',blank=False,null=False,auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name='Modelo2'
        verbose_name_plural='Modelos2'

    def __str__(self):
        return self.nombre



