from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import time

from .forms import AutorForms
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

"""Vistas Basadas en funciones:
        son aquellas toda su logica se maneja
        en sintaxis python """


def libro(request):
    return render(request,'libro/prueba.html')

# Create your views here.
def Home(request):
    #all_autor = Autor.objects.all()
    all_autor = Autor.objects.filter(estado=True)

    return render(request,'libro/all_autor.html',{'autor':all_autor})

def createAutor(request):

    if request.method == 'POST':
        autor_form = AutorForms(request.POST)

        # con los datos dentro validamos si son correctos
        # y corresponden a lo que tiene el mode
        if autor_form.is_valid():
            autor_form.save()
 
            return redirect('/home')

    autor_form =  AutorForms()   
    return render(request,'libro/crear_autor.html',{'form':autor_form})  



def listarAutor(request):

# organizamos para eliminacion logica     
#    all_autor = Autor.objects.all()   #utilizo El Orm 


    all_autor = Autor.objects.filter(estado=True) 
    print('Que me llega de la base de datos aqui    ',all_autor)
    return render(request,'libro/all_autor.html',{'autor':all_autor}) 




def editar_autor(request,id):

    #definimos esta variable para que no me saque el
    # error de que lo mostramos antes de definirlo
    autor_forms = None
    error = None
    
    try:
        autor = Autor.objects.get(id=id)

        if request.method == 'GET':
            print('entra primero por aca ')
            autor_forms= AutorForms(instance=autor)

        else:
            autor_forms = AutorForms(request.POST,instance=autor)

            if autor_forms.is_valid():

                autor_forms.save()
                return redirect('/home')
            
           
    except ObjectDoesNotExist  as e:
        error = e

    return render(request,'libro/crear_autor.html',{'form':autor_forms,'error':error}) 



# """
#  Eliminacion  por id 
#  consta de recibir un id y buscar el
#  modelo en la base de datos una ves encontrado
#  se elimina """
# def eliminar_autor(request,id):
#     auto_to_delete = Autor.objects.get(id=id)
#     auto_to_delete.delete()
#     """   
#     creamos un redireccionamiento para que me lleve al 
#     a las views donde tengo el endpoind que me lleva 
#     al html para ver todos los usuarios
#     Alli en las htmls ponemos un boton para eliminar desde alli
#     """
#     return redirect('libro:autores')

# """Eliminar por metodo Post :
#    Esto significa que haremos una peticion primero desde el 
#    listado de usuarios con un boton para eliminar
#    -este botton nos redireccionara 
#    - a la vista eliminar donde hay una condicion preguntando
#      si es un metodo post el cual la primer ves no sera 
#      entonces pasara por la segunda condicion o return dond
    
#     - nos llevara a un htm donde eviamos el modelo
#     - en este html creamos el post con el csr y form post
#     - para preguntar si se desea eliminar si es si 
#       nos redireccionara nuevamente a la vista que ahora si entrara por
#       el post y eliminar y el id le llegara por que 
#       lla lo hemos enviado desde la lista inicial ya que pasa primero
#       por alli
#       si damos en no borrar me devuelve a la lista nuevamente y no pasa nada 
#    """
# def  eliminar_autor(request,id):
#     autor_to_delete = Autor.objects.get(id=id)

#     """Verificamos si es metodo post"""
#     if request.method == 'POST':
#         """si es un metodo post eliminamos 
#            y luego nos redireccionamos a la
#            url que me lleva a ver todos lo autores"""
#         autor_to_delete.delete()
#         return redirect('libro:autores')
    
#     """cuando se haga todo el proceso renderizamos
#        a un nuevo template para pedir una verificacion
#        y alli mandamos el modelo para utilizarlo para 
#        validaciones del modelo que boy a eliminar 
#        """
#     return render(request,'libro/eliminar_autor.html',{'autor':autor_to_delete})
    


"""Eliminacion logica:

        lo que hace la eliminacion logica es cambiar el 
        estado de una variable en mi modelo para 
        que cuando el usuario de eliminar ponga 
        el estado del modelo en false y no lo muestre
        pero realmente no lo elimina de la basede datos 
        solo lo oculta"""

"""modificaciones:
        1 crear un campo de estado 
        2 en listar autores solo los boy a mostrar 
          por lo que tienen estado activo 
        3"""
def eliminar_autor(request,id):

    autor_to_delete = Autor.objects.get(id=id)
    if request.method == 'POST':
        
            """llamamos el atributo estado del 
            modelo el que creamos alli y le cambiamos
            el true por un false """
            autor_to_delete.estado = False

            """luego de cambiar el estado guardamos 
            los cambios para que se actualizen en model
            y esta seria la eliminacion logica """
            autor_to_delete.save()
            
            return redirect('libro:autores')
    
    return render(request,'libro/eliminar_autor.html',{'autor':autor_to_delete})


