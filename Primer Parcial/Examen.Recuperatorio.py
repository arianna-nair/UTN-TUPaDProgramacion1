titulo=[]
ejemplar=[]
continuar= True
menu=""
agotados=""
continuar_programa= True
encontrado=False
crear_base_de_datos= input("Para realiar el ingreso inicial de titulos ingrese 'inicio': ")
if crear_base_de_datos.lower() == "inicio":
    while continuar==True:
        libro= input("Nombre del libro: ")
        if libro.strip()=="":
            print("Debe ingresar un titulo")
            libro= input("Nombre del libro: ")
        titulo.append(libro)
        cantidad= int(input("Cantidad de  ejemplares: "))
        if cantidad < 0:
            print("Debe ingresar un numero positivo")
            cantidad= int(input("Cantidad de  ejemplares: "))
        ejemplar.append(cantidad)
        finalizar= input("Para finalizar el ingreso, ingrese 'ok', sino, presione la tecla 'Enter'")
        if finalizar.lower()== "ok":
            continuar=False
        else:
            continuar=True
for i in range(len(titulo)):
    indice_titulo=titulo[i]
    indice_ejemplares=ejemplar[i]
    menu += indice_titulo + "----------" + str(indice_ejemplares) + "\n"
while continuar_programa == True:
    accion= input("Para ver Stock ingrese 'stock'/\nPara consultar disponibilidad ingrese 'disponible'/\nPara ver el listado de titulos con ejemplares agotados ingrese 'agotados'/\nPara agregar un titulo a la base de datos ingrese 'agregar'/\nPara efectuar prestamos o devoluciones ingrese 'modificar': ")
    if accion.lower()=="stock":
        print(menu)
        salir= input("Para volver al menu principal ingrese 'menu'/\nPara salir del programa ingrese 'salir': ")
        if salir.lower()=="menu":
            continuar_programa=True
        else:
            continuar_programa=False
            print("Fin del programa")
    if accion.lower()=="disponible":
        buscar= input("Ingrese el nombre del libro que desea buscar: ")
        for i in range(len(titulo)):
            if titulo[i].lower() == buscar.lower():
                print(titulo[i] + "----------" + str(ejemplar[i]))
                encontrado=True
                break
            if not encontrado:
                print(f"{buscar} no se encuentra en la base de datos")
                agregar_libro= input("Si desea agregar el libro a la base de datos ingrese 'agregar', sino presione la tecla 'Enter': ")
                if agregar_libro.lower() == "agregar":
                    libro_agregar= input("Ingrese el nombre del libro: ")
                    titulo.append(libro_agregar)
                    ejemplar_libro= input("Ingrese la cantidad de ejemplares: ")
                    ejemplar.append(ejemplar_libro)
                    menu += libro_agregar + "----------" + str(ejemplar_libro) + "\n"
                    print(menu)
                    break
                else:
                    salir= input("Para volver al menu principal ingrese 'menu'/\nPara salir del programa ingrese 'salir': ")
                    if salir.lower()=="menu":
                        continuar_programa=True
                    else:
                        continuar_programa=False
                        print("Fin del programa")
    if accion.lower() == "agotados":
        for i in range(len(titulo)):
            if ejemplar[i] == 0:
                print(titulo[i], "--- Agotado")
        salir= input("Para volver al menu principal ingrese 'menu'/\nPara salir del programa ingrese 'salir': ")
        if salir.lower()=="menu":
            continuar_programa=True
        else:
            continuar_programa=False
            print("Fin del programa")
    if accion.lower() == "agregar":
        libro_agregar= input("Ingrese el nombre del libro: ")
        titulo.append(libro_agregar)
        ejemplar_libro= input("Ingrese la cantidad de ejemplares: ")
        ejemplar.append(ejemplar_libro)
        menu += libro_agregar + "----------" + str(ejemplar_libro) + "\n"
        print(menu)
        salir= input("Para volver al menu principal ingrese 'menu'/\nPara salir del programa ingrese 'salir': ")
        if salir.lower()=="menu":
            continuar_programa=True
        else:
            continuar_programa=False
            print("Fin del programa")
    if accion.lower()=="modificar":
        buscar_libro= input("Libro: ")
        encontrado=False
        for i in range(len(titulo)):
            if titulo[i].lower() == buscar_libro.lower():
                encontrado=True
                opcion= input("Para prestamos presione 'p', para devoluciones, 'd': ")
                if opcion.lower() == "p":
                    if ejemplar[i] > 0:
                        ejemplar[i] -= 1
                        print(f" Ahora hay {ejemplar[i]} ejemplares de '{titulo[i]}'.")
                    else:
                        print(f"No hay ejemplares disponibles de '{titulo[i]}' para préstamo.")
            
                elif opcion.lower() == "d":
                    ejemplar[i] += 1
                    print(f"Ahora hay {ejemplar[i]} ejemplares de '{titulo[i]}'.")
            
                else:
                    print("Opcion invalida")
                break
        if not encontrado:
            print("Libro no encontrado")
        salir= input("Para volver al menu principal ingrese 'menu'/\nPara salir del programa ingrese 'salir': ")
        if salir.lower()=="menu":
            continuar_programa=True
        else:
            continuar_programa=False
            print("Fin del programa")  
