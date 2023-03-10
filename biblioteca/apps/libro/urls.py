from django.urls import path
from .views import Home,libro,createAutor,listarAutor,editar_autor,eliminar_autor

# como funciona esto explique parte por parte :

#path('home/',Home,name='home'),

urlpatterns=[

    path('libro/',libro,name='index'),
    path('',Home,name='home'),
    path('crear_autor/',createAutor,name='crear_autor'),
    path('lista_autores/',listarAutor,name='autores'),
    path('editar/<int:id>',editar_autor,name='editar'),
    path('eliminar/<int:id>',eliminar_autor,name='eliminar')


]