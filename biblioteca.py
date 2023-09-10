from libro import * 

titulo = ["El ultimo gol","El algortmo del mal","El primer gol"]
autor = ["Messi","Nicolas Surgen","Messi"]
genero = ["Deportes","Programación","Deportes"]
cantidad = [10,5,15] 
biblioteca = []
for t,a,g,c in zip(titulo,autor,genero,cantidad):
    biblioteca.append({
                        "Título": t,
                        "Autor": a,
                        "Género": g,
                        "Cantidad de copias disponibles": c
                })

print(BuscarLibro(biblioteca))

