from typing import List,Tuple,Dict
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
    
    
def PrestarLibro(biblioteca: List[Dict],usuariosreg: List[str],librosprestados: List[Dict]):
    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        print(f"Su nombre de usuario es: {usuario}?")
        while True:
            decicion = input()
            decicion = decicion.lower()
            if decicion in ["si","no"]:
                break
            else:
                print("Elija una opcion valida")
        if decicion == "si":
            break
    if usuario in usuariosreg:
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
        for libro in biblioteca:
            if libro.get("Título") == prestar:
                if libro.get("Cantidad de copias disponibles") > 0:
                    libro["Cantidad de copias disponibles"] -= 1
                    librosprestados.append({"Usuario":usuario,
                                            "Libro Prestado": prestar
                                            })
                    print(f"Se le ha prestado una copia del libro {prestar} al usuario {usuario}")
                else:
                    print(f"No quedan copias disponibles del libro {prestar}")
            else:
                print("No poseemos ese libro en nuestra biblioteca")
    else:
        print("Ese usuario no se encuentra registrado")            