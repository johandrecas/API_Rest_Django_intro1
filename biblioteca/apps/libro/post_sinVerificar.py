# def createAutor(request):

#     # verificamos si el method es Post
#      if request.method == 'POST':

#         #traemos el formulario creado e en forms 
#         # perteneciente a el modelo que estoy creando
#         # ya que su estructura nos guadara los 
#         # datos en el modelo los datos ya los trae el request
#         # en request.POST y sera los que le pasamos al modelo form
#         # para que lo cree 
#         autor_form = AutorForms(request.POST)
    
#         # verificamos con uno de los metodos de forms
#         #  si los datos 
#         # ingresados fueron validos este metodo verifica 
#         # que la informacion coincida y sea validad segun 
#         # definimos en el modelo original
#         if autor_form.is_valid():

#             # si la verificacion es correcta 
#             # utilizamos redirect para que nos redireccione 
#             # a este enpoind  o pagina que que debe 
#             # coincidir con los que anote en 
#             # mir urls name='libro'  que asu ves me llevan a 
#             # vistas que nos llevan a otros html o directamente
#             # a este html asociado

#              return redirect('index')
        
#         #Pero si no es un metodo post entonces quiere decir 
#         #que lo debo redireccionar a la pagina para que me lo cree
#         # de una ves 
#         else:

#             # envio modelo o formulario para ser llenado y 
#             # envio estos datos al htm con el formulario para ser 
#             #  llenado alli y luego crearlo
#             autor_form =  AutorForms()

#         # si no es un metodo post redireccionamos a un html con el modelo
#         # para pintarlo y llenarlo
#         # 
#         return render(request,'libro/crear_autor.html',{'autor_form':autor_form})
