peliculas = []
def agregar_peliculas():
    cantidad_peliculas = int(input("Ingrese cuantas peliculas desea ingresar al catalogo: "))
    for i in range(cantidad_peliculas):
        titulo = input("Ingrese el titulo de la pelicula: ")
        año = int(input("Ingrese el año de estreno: "))
        genero = input("Ingrese el genero de la pelicula: ")
        peliculas.append([titulo, año, genero])
        print("-"*20)
    print("Pelicula agregada")
def mostrar_peliculas():
    if not peliculas:
        print("No hay peliculas agregadas al catalogo")
        return
    print("-----Catalogo de peliculas-----")
    for i in peliculas:
        print(f"-Titulo: {i[0]}, Año: {i[1]}, Genero: {i[2]}")
        print("-"*20)
def buscar_peliculas_genero():
    genero = input("Ingrese el genero que desea buscar: ")
    genero_encontrado = False
    for i in peliculas:
        if i[2].lower() == genero.lower():
            print(f"Nombre: {i[0]},Año: {i[1]}")
            genero_encontrado=True
    if not genero_encontrado:
        print("No hay peliculas de ese genero.")
    print("-"*20)
def eliminar_pelicula():
    titulo= input("Ingrese el titulo de la pelicula a eliminar")
    titulo_encontrado=False

    for i in peliculas:
        if i[0].lower()== titulo.lower():
            peliculas.remove(i)
            titulo_encontrado=True
            print(f"Pelicula {titulo} eliminada del catalogo")
    if not titulo_encontrado:
        print(f"No se encontro la pelicula {titulo} en el catalogo")
        print("-"*20)
def mostrar_estadisticas():
    if not peliculas:
        print("No hay peliculas registradas")
    else:
        print(f"Total de peliculas registradas: {len(peliculas)}")
        generos=[]
        print("---Peliculas por generos---")
        for i in peliculas:
            genero = i[2].lower()
            if genero not in generos:
                generos.append(genero)
                contador =0
                for j in peliculas:
                    if j[2].lower()==genero:
                        contador +=1
                print(f"-{genero}: {contador}")
        if peliculas:
            antigua = peliculas[0]
            for i in peliculas:
                if i[1]< antigua[1]:
                    antigua=i
            print(f"Pelicula mas antigua: {antigua[0]}-{antigua[1]}")
    print("-"*20)
while True:
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
        case "3":
            buscar_peliculas_genero()
        case "4":
            eliminar_pelicula()
        case "5":
            mostrar_estadisticas()

