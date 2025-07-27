peliculas = []
while True:
    print("-"*20)
    print("Catalogo de peliculas")
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
            cantidad_peliculas =  int(input("Ingrese cuantas peliculas desea ingresar al catalogo: "))
            for i in range(cantidad_peliculas):
                titulo = input("Ingrese el titulo de la pelicula: ")
                año = int(input("Ingrese el año de estreno: "))
                genero= input("Ingrese el genero de la pelicula: ")
                peliculas.append([titulo,año,genero])
                print("Pelicula agregada")

