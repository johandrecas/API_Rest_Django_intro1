from django.db import models

# Create your models here.
class Autor(models.Model):

    """aqui le indicamo que sea auto incremental """
    id = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=200,blank=False,null=False)
    nombre = models.CharField(max_length=200,blank=False,null=False)
    nacionalidad = models.CharField(max_length=200,blank=False,null=False)

    # lo usamos para cambiar el estado y hacer eliminaciones logicas 
    estado = models.BooleanField('Estado',default=True) 
    

    """Este campo es para que no me limite la cantidad de escritura """
    descripcion = models.TextField(blank=False,null=False)

   #El argumento auto_now se utiliza para actualizar
   #  automáticamente el campo con la fecha
   #  y hora actuales cada vez que se guarda
   #  o modifica el objeto del modelo.
   #auto_now_add se utiliza para establecer automáticamente
   #  el campo con la fecha y hora actuales en el momento en 
   #  que se crea el objeto del modelo
    fecha_creacion = models.DateField('Fecha Creacion',blank=False,null=False,auto_now=True,auto_now_add=False)


    #En particular, los atributos verbose_name
    #  y verbose_name_plural de la clase Meta se
    #  utilizan para proporcionar nombres
    #  humanamente legibles para un modelo
    #  y su plural, respectivamente
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authores'

    # La función def __str__(self) se utiliza en Django
    #  para proporcionar una representación legible de
    #  los objetos de un modelo en el panel de
    #  administración de Django. :
    def __str__(self):
        return self.nombre


class libro(models.Model):
    # le creamos el identificador unico para poderlo 
    # encontrar esta es como su cedula
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=34,blank=True,null=True)
    fecha_publicacion = models.DateTimeField('Fecha publicacion',blank=False,null=False)
    author_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha Creacion',blank=False,null=False,auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name='libro__'
        verbose_name_plural='libros__'

    def __str__(self):
        self.titulo
  