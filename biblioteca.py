from libro import * 

titulo = ["El ultimo gol","El algoritmo del mal","El primer gol","Alicia"]
autor = ["Messi","Nicolas Surgen","Messi","Charly"]
genero = ["Deportes","Programación","Deportes","Fantasia"]
cantidad = [10,3,15,2] 
biblioteca = []
for t,a,g,c in zip(titulo,autor,genero,cantidad):
    biblioteca.append({
                        "Título": t,
                        "Autor": a,
                        "Género": g,
                        "Cantidad de copias disponibles": c
                })

identificadores = [141024]

usuarios = [{
                "Identificador": 141024,
                "Nombre": "Nicolas",
                "Libros Prestados": ["Alicia","El ultimo gol"]
                }]


print(biblioteca)
print()
print(usuarios)
print()
print(identificadores)
print()
PrestarLibro(biblioteca,usuarios)
DevolverLibro(biblioteca,usuarios)
print()
print(biblioteca)
print()
print(usuarios)
print()
print(identificadores)
print()



