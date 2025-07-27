peliculas = []
def agregar_peliculas():
    cantidad_peliculas = int(input("Ingrese cuantas peliculas desea ingresar al catalogo: "))
    for i in range(cantidad_peliculas):
        titulo = input("Ingrese el titulo de la pelicula: ")
        año = int(input("Ingrese el año de estreno: "))
        genero = input("Ingrese el genero de la pelicula: ")
        peliculas.append([titulo, año, genero])
    print("Pelicula agregada")
def mostrar_peliculas():
    if not peliculas:
        print("No hay peliculas agregadas al catalogo")
        return
    print("Catalogo de peliculas")
    for i in peliculas:
        print(i)

while True:
    print("-"*20)
    print("Menu")
    print("1. Agregar peliculas")
    print("2. Mostrar peliculas registradas")
    print("3. Buscar peliculas por genero")
    print("4. Eliminar una película")
    print("5. Ver estadisticas")
    print("6. Salir")
    print("-"*20)
    opcion = input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            agregar_peliculas()
        case "2":
            mostrar_peliculas()
