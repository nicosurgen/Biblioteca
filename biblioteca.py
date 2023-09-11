from app import api 


# Información sobre los libros
titulo = ["Te regalo un teorema","Harry Potter y la piedra filosofal","Cien años de soledad","Heartstopper Tomo 1","Orgullo y prejuicio",
          "El señor de los anillos el retorno del rey","Crimen y castigo","Indigno de ser humano"]

autor = ["Pablo Groisman","J.K.Rowling","Gabriel García Márquez","Alice Oseman","Jane Austen","Tolkien J.R.R","Fiódor Dostoyevski","Osamu Dazai"]

genero = ["Educación",["Fantasía","Aventura"],["Ficción","Realismo magico"],"Amor",["Novela", "Ficción", "Romance"],
          ["Alta fantasía", "Ficción de aventuras"],["Policial", "Novela filosófica"],["Novela", "Ficción"]]

cantidad = [10,15,5,6,6,9,15,2] 
biblioteca = []
for t,a,g,c in zip(titulo,autor,genero,cantidad):
    biblioteca.append({
                        "Título": t,
                        "Autor": a,
                        "Género": g,
                        "Cantidad de copias disponibles": c
                })

# Información sobre usuarios
ids = [241724,666666,767899,285102,998833,224466]
nombres = ["Nicolas","Catalina","Juan Cruz","Noelia","Ramiro","Rocio"]
librosprestados = [["Indigno de ser humano","Te regalo un teorema","El señor de los anillos el retorno del rey"],
                   ["Crimen y castigo","Orgullo y prejuicio"],
                   ["Harry Potter y la piedra filosofal"],
                   ["Heartstopper Tomo 1"],
                   [],
                   ["Harry Potter y la piedra filosofal"]]

usuarios = []

for i,n,l in zip(ids,nombres,librosprestados):
    usuarios.append({
                "Identificador": i ,
                "Nombre": n,
                "Libros Prestados": l
                })

identificadores = [x["Identificador"] for x in usuarios]

"""
ESPACIO PARA PROBAR LA API

print(api(Biblioteca= biblioteca, Usuarios= usuarios, Identificadores= identificadores))

"""

