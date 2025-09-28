titulos=[]
ejemplares=[]
faltantes=[]
continuar_programa=True
continuar=True
crear_base_de_datos= input("Para hacer el ingreso inicial de los libros disponibles ingrese 'inicio'")
if crear_base_de_datos == "inicio":
        continuar=True
        while continuar == True:
                libro= input("Nombre del libro: ")
                titulos.append(libro)
                cantidad=int(input("cantidad de ejemplares: "))
                ejemplares.append(cantidad)
                seguir= input("Ingrese 'salir', para cerrar el ingreso, sino presione 'Enter'.")
                if seguir=="salir":
                    continuar=False 
                else:
                    continuar==True
        print("---------------MENU---------------")
        menu=""
        for i in range(0,len(titulos)):
            indice_titulo=titulos[i]
            indice_ejemplares=ejemplares[i]
            menu +=indice_titulo + "-----" + str(indice_ejemplares) +"\n"
        print(menu)
        menu_oficial= menu
while continuar_programa==True:
    ingreso_inicial= input("/\nPara consultar disponibilidad ingrese 'buscar'/\nPara ver el Menu ingrese 'menu'/\nPara ver los libros con ejemplares agotados ingrese 'faltante'/\nPara agregar libros a la base de datos ingrese 'agregar'/Para registrar prestamos o devoluciones ingrese 'stock")

    if ingreso_inicial == "menu":
        print(menu_oficial)

    continuar=True
    while continuar==True:
        if ingreso_inicial == "buscar":
            buscar_libro= input("Ingrese el nombre del libro que desea buscar: ").lower()
            busqueda=False
            for i in range (len(titulos)):
                if titulos[i].lower() == buscar_libro:
                    encontrado= titulos[i] + "-----" + str(ejemplares[i])
                    print(encontrado)
                    busqueda=True
                    break
            if not busqueda:
                print(f"{buscar_libro} no se encuentra en la base de datos")
                nueva_opcion= input("¿Desea buscar otro libro o cargar el libro que busca a la base de datos? Agregar / Buscar").lower()
                if nueva_opcion.lower() == "Agregar":
                    continuar = False
                    continue
                else: 
                    continuar=True 

        if ingreso_inicial == "faltante":

            continuar = True
while continuar == True:
    faltantes=[] 
    for i in range(len(titulos)):
        if ejemplares[i] == 0:
            faltantes.append(titulos[i])
    if len(faltantes) == 0:
        print("No hay libros agotados")
    else:
        print("Libros agotados:")
        for libro in faltantes:
            print("-", libro)
    continuar = False
if ingreso_inicial == "agregar" or nueva_opcion == "agregar":
    continuar = True
    while continuar == True:
        agregar_libro = input("Ingrese el título del libro que quiere ingresar: ")
        titulos.append(agregar_libro)
        agregar_ejemplares = int(input(f"Ingrese cantidad de ejemplares para {agregar_libro}: "))
        ejemplares.append(agregar_ejemplares)
        menu_oficial = ""
        for i in range(len(titulos)):
            menu_oficial += titulos[i] + " ----- " + str(ejemplares[i]) + "\n"
        print(menu_oficial)
        seguir_agregando = input("¿Quiere agregar otro libro? (si/no): ").lower()
        if seguir_agregando != "si":
            continuar = False
if ingreso_inicial=="stock":
    libro_seleccionado = input("Ingrese el nombre del libro que desea: ").lower()
    encontrado = False
    for i in range(len(titulos)):
        if titulos[i].lower() == libro_seleccionado:
            encontrado = True
            accion = input("Ingrese 'prestamo' para sacar un ejemplar o 'devolucion' para sumar uno: ").lower()
            
            if accion == "prestamo":
                if ejemplares[i] > 0:
                    ejemplares[i] -= 1
                    print(f" Ahora hay {ejemplares[i]} ejemplares de '{titulos[i]}'.")
                else:
                    print(f"No hay ejemplares disponibles de '{titulos[i]}' para préstamo.")
            
            elif accion == "devolucion":
                ejemplares[i] += 1
                print(f"Ahora hay {ejemplares[i]} ejemplares de '{titulos[i]}'.")
            
            else:
                break
volver=input("Para volver al menu principal ingrese 'volver'")
if volver != "volver":
        continuar_programa = False
        print("Fin del programa")
