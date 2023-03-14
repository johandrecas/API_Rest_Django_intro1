from django.contrib import admin
from .models import Autor,libro

"""2.para que sirve resources.
    proporciona una interfas grafica para saber
    como importamos y exportamos los datos donde 
    crearemos una clase donde definiremos los 
    datos para hacer esto como una plantilla """
from import_export import resources

"""proporciona una interfas
   grafica para la importacion
   y exportacion brindando botones 
   en el admin para hacerl"""
from import_export.admin import ImportExportActionModelAdmin


"""1.para que sirve import-export:
        permitir la importación
        y exportación de datos en
        varios formatos como CSV,
        Excel, JSON y otros.
   para que utilizo import-export 
   pasos para configurar
        admin
            import resources
            import  ImportExportActionModelAdmin
            creacion clase 
            vincularla con mi categoria model de cada 
            modelo 
            pasarle a mi clase categoria modelo herencia 
            de import export para que funcione y quede todo vinculado 
            en la pantalla del admin 
            y con esto podremos importar y exportar en el 
            formato que queramos nuestros archivos """

class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Autor

class categoriaAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion')
    resource_class = CategoriaResources


admin.site.register(Autor,categoriaAdmin)

class CategoriaResourcesLibro(resources.ModelResource):
    class Meta:
        model= libro

"""para poder pasarle la funcion de import y export debemos heredarle
   la clase que importamos y que heredamos previamente si no no work"""
class categoriaAdminLibro(ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields=['nombre']
    list_display=('titulo','fecha_publicacion','fecha_creacion')
    resource_class = CategoriaResourcesLibro


admin.site.register(libro,categoriaAdminLibro)
