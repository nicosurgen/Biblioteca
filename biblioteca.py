from libro import * 

titulo = ["El ultimo gol","El algoritmo del mal","El primer gol"]
autor = ["Messi","Nicolas Surgen","Messi"]
genero = ["Deportes","Programación","Deportes"]
cantidad = [10,3,15] 
biblioteca = []
for t,a,g,c in zip(titulo,autor,genero,cantidad):
    biblioteca.append({
                        "Título": t,
                        "Autor": a,
                        "Género": g,
                        "Cantidad de copias disponibles": c
                })

usuarios = ["Nicolas","Juan Cruz"]
prestados = [{"Usuario":"Nicolas","Libros Prestados":10}]

PrestarLibro(biblioteca,usuariosreg=usuarios,librosprestados= prestados)
print()
print(biblioteca)
print(prestados)

#print(biblioteca[1].get("Título") == "El algoritmo del mal")
