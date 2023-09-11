from typing import List,Tuple,Dict
import random
"""
Escribe un programa en el lenguaje de programación que prefieras para gestionar una colección de libros. Debes ser capaz de realizar las siguientes operaciones:

- Agregar un nuevo libro a la colección con información como título, autor, género y número de copias disponibles.
- Buscar un libro por título o autor y mostrar su información.
- Prestar un libro a un usuario registrado (reducir el número de copias disponibles).
- Devolver un libro prestado (aumentar el número de copias disponibles).
- Registrar usuarios de la biblioteca con información como nombre, número de identificación y libros prestados.
- Mostrar la información de un usuario, incluyendo los libros que ha prestado.
- Mostrar una lista de todos los libros en la colección.
- Mostrar una lista de todos los usuarios registrados en la biblioteca.

"""

def AgregarLibro(Biblioteca:List[Dict]):
    while True:
        titulo = input("Ingrese el título del libro: ")
        autor =  input("Ingrese el autor del libro: ")
        genero = input("Ingrese el genero del libro: ")
        while True:
                    try:
                        ncopias = int(input("Ingrese el número de copias disponibles del libro: "))
                        if ncopias >= 0:
                            break
                        else:
                            print("Tenes que ingresar una cantidad válida")
                    except: 
                        print("Tenes que ingresar una cantidad válida")
        libro = {
                        "Título":titulo,
                        "Autor":autor,
                        "Género":genero,
                        "Cantidad de copias disponibles":ncopias
                }
        print(libro)
        while True:
            decicion = input("La información es correcta: ")
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
        if decicion == "si":
            break
    Biblioteca.append(libro)
 
# Función para la búsqueda de libros
   
def BuscarLibro(Biblioteca:List[Dict]):
    while True:
        print("Seleccione su opción de búsqueda:\n* 1-Búsqueda por título.\n* 2-Búsqueda por autor.")
        try:
            metodo = int(input())
            if metodo in [1,2]:
                break
            else:
                print("Elige una opción válida")
        except:
            print("Elige una opción válida")
            
    # Búsqueda por Título
    
    if metodo == 1:
        while True:
            titulo = input("Ingrese el título a buscar: ")
            print(f"¿El título que quieres buscar es: {titulo}?")
            while True:
                decicion = input()
                decicion = decicion.lower()
                if decicion in ["si","no"]:
                    break
                else:
                    print("Elija una opcion valida")
            if decicion == "si":
                break
        resultado = "No se ha encontrado libro que posea ese título"
        for libro in Biblioteca:
            if libro.get("Título") == titulo:
                resultado = libro
                break
            
        return resultado
    
    # Búsqueda por autor
    
    if metodo == 2:
        while True:
            autor = input("Ingrese el autor a buscar: ")
            print(f"¿El autor que quieres buscar es: {autor}?")
            while True:
                decicion = input()
                decicion = decicion.lower()
                if decicion in ["si","no"]:
                    break
                else:
                    print("Elija una opcion valida")
            if decicion == "si":
                break
        resultado = []
        
        for libro in Biblioteca:
            if libro.get("Autor") == autor:
                resultado.append(libro)   
        if len(resultado) == 1:
            resultado = resultado[0]  
        if resultado == []:
            resultado = "No se ha encontrado libro escrito por dicho autor en nuestra biblioteca"
            
        return resultado
    
 
# Funcion para el prestamo de libros
    
def PrestarLibro(biblioteca: List[Dict], Usuarios: List[Dict]):
    while True:
        
        while True:
            try:
                ident = int(input("Ingrese su identificador de usuario: "))
                break
            except:
                print("Ingrese un identificador válido")
                
        usuario = input("Ingrese su nombre de usuario: ")
        print(f"Su identificador y nombre son: {ident} y {usuario}?")
        while True:
            decicion = input()
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
            else:
                print("Elija una opcion valida")
        if decicion == "si":
            break
    ids = [Id["Identificador"] for Id in Usuarios]
    if ident in ids:
        for user in Usuarios:
            if user.get("Identificador") == ident and len(user.get("Libros Prestados")) >= 5:
                print(f"Operación denegada, el usuario {usuario} debe devolver {len(user.get('Libros Prestados'))} libros que le han sido prestados")
                return
           
        while True:
            print("¿Cual es el título del libro que se va a prestar?")
            prestar = input()
            print(f"Se va a prestar el libro: {prestar}?")
            while True:
                decicion = input()
                decicion = decicion.lower()
                if decicion in ["si","no"]:
                    break
                else:
                    print("Elija una opcion valida")
            if decicion == "si":
                break
        NoExiste = True
        for libro in biblioteca:
            if libro.get("Título") == prestar:
                if libro.get("Cantidad de copias disponibles") > 0:
                    libro["Cantidad de copias disponibles"] -= 1
                    
                    for user in Usuarios:
                        if user.get("Identificador") == ident:
                            user["Libros Prestados"].append(prestar)
                            
                    NoExiste = False
                    print(f'Se le ha prestado una copia del libro "{prestar}" al usuario {usuario}')
                    break
                else:
                    print(f"No quedan copias disponibles del libro {prestar}")
        if NoExiste:
            print("No poseemos ese libro en nuestra biblioteca")
    else:
        print("Ese usuario no se encuentra registrado")     
        
        
# Función para devolver los libros        
def DevolverLibro(biblioteca: List[Dict], Usuarios: List[Dict]):
    while True:
        
        while True:
            try:
                ident = int(input("Ingrese su identificador de usuario: "))
                break
            except:
                print("Ingrese un identificador válido")
                
        usuario = input("Ingrese su nombre de usuario: ")
        print(f"Su identificador y nombre son: {ident} y {usuario}?")
        while True:
            decicion = input()
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
            else:
                print("Elija una opcion valida")
        if decicion == "si":
            break
    
    while True:
        print("¿Que libro va a devolver?")
        libro = input()
        print(f"Se va a devolver el libro: {libro}?")
        while True:
            decicion = input()
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
            else:
                print("Elija una opcion valida")
        if decicion == "si":
            break
        
    flag = True
    for user in Usuarios:
        if user.get("Identificador") == ident:
            if libro in user.get("Libros Prestados"):
                flag = False
                user["Libros Prestados"].remove(libro)
                print(f"El libro {libro} ha sido devuelto con éxito")
                        
                for lib in biblioteca:
                    if lib.get("Título") == libro:
                            lib["Cantidad de copias disponibles"] += 1
    if flag:
        print(f"El usuario {usuario} no debe el libro {libro}")
        
# nombre, número de identificación y libros prestados.
        
def RegistrarUsuario(Usuarios:List[Dict], ListaDeIdentificadores: List[int]):
    # Solicitar datos del nuevo usuario
    while True:
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        # Solicitar ingresar un identificador de 6 dígitos
        while True:
            try:
                identificador = input("Ingrese el idenficador de 6 dígitos: ")
                if len(identificador) == 6:
                    identificador = int(identificador)
                    if identificador in ListaDeIdentificadores:
                        for i in Usuarios:
                            if i.get("Identificador") == identificador and i.get("Nombre") == nombre: 
                                print(f"El usuario {nombre} ya se encuentra registrado")
                                return
                        print("Ese identificador ya se encuentra en uso")
                        return
                    else:
                        ListaDeIdentificadores.append(identificador)
                        break
                else:
                    print("El identificador debe tener 6 dígitos")
            except:
                print("Escribi un identificador válido")
        
        print(f"Su nombre de usuario es: {nombre}?")
        while True:
            decicion = input()
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
            else:
                print("Elija una opcion valida")
        
        if decicion == "si":
            break
        ListaDeIdentificadores.remove(identificador)
    # Desarrollo el usuario con los datos proporcionados
    usuario = {
                "Identificador": identificador,
                "Nombre": nombre,
                "Libros Prestados": []
                }
    # Agrego al usuario a la base
    Usuarios.append(usuario)



