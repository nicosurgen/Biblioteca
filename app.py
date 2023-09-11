from libro import * 
from typing import List,Tuple,Dict

# Creo la aplicación que reune todas las funcionalidades

def api(Biblioteca:List[Dict], Usuarios:List[Dict], Identificadores: List[int]):
    opciones = [i for i in range(1,10)]
    
    while True:
        print("Que opción desea realizar:\n 1.- Buscar un libro. \n 2.- Buscar un Usuario. \n 3.- Agregar un Usuario. \n 4.- Agregar un libro. \n 5.- Realizar un prestamo. \n 6.- Registrar una devolución. \n 7.- Obtener lista de libros. \n 8.- Eliminar un usuario \n 9.- Obtener lista de usuarios")
        try:
            opcion = int(input())
            if opcion in opciones:
                break
            else:
                print("Elegí una de las opciones válidas")
        except:
            print("Tenes que elegir una de las opciones válidas")
    
    # Buscar un libro
    if opcion == 1:
        return BuscarLibro(Biblioteca)
    
    # Buscar un Usuario
    elif opcion == 2:
        return BusquedaUsuario(Usuarios)
    
    # Agregar un Usuario
    elif opcion == 3:
        RegistrarUsuario(Usuarios,Identificadores)
        
    # Agregar un libro
    elif opcion == 4:
        AgregarLibro(Biblioteca)
        
    # Realizar un prestamo
    elif opcion == 5:
        PrestarLibro(Biblioteca, Usuarios)
        
    # Registrar una devolución
    elif opcion == 6:
        DevolverLibro(Biblioteca, Usuarios)
    
    # Obtener lista de libros
    elif opcion == 7:
        return  LibrosBiblio(Biblioteca)
    
    elif opcion == 8:
        EliminarUsuario(Usuarios,Identificadores)
     
    # Obtener lista de usuarios   
    else:
        return Users(Usuarios)