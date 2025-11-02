import csv
import os 
NOMBRE_ARCHIVO= "titulos01.csv"
def mostrar_menu():
    while True:
        print("Mostrar catalogo--------------1\nIngresar titulos--------------2\nModificar ejemplares--------------3\nConsultar disponibilidad--------------4\nListar agotados--------------5\nPrestamos--------------6\nDevoluciones--------------7\nSalir--------------8")
        opcion=input("Ingrese una opcion:").strip()
        match opcion:
            case "1":
                mostrar_titulos()
            case "2":
                nuevos_titulos()
            case "3":
                modificar_ejemplares()
            case "4":
                disponibilidad()
            case "5":
                listar_agotados()
            case "6":
                prestamos()
            case "7":
                devoluciones()
            case "8":
                salir()
                break
            case _:
                print("La opcion indicada no es valida")
def obtener_titulos():
    titulos = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Cantidad"])
            escritor.writeheader()
            cantidad_titulos = int(input("¿Cuántos ejemplares querés agregar?: "))
            cont = 1
            while cont <= cantidad_titulos:
                ingresar_titulo = input("Título: ")
                if any(t.lower() == ingresar_titulo.lower() for t in titulos):
                    print("Este título ya fue ingresado. Intente con otro.")
                    continue
                ingresar_cantidad = int(input("Cantidad: "))
                if ingresar_cantidad<0:
                    print("Debe ingresar un numero positivo de ejemplares")
                escritor.writerow({"Nombre": ingresar_titulo, "Cantidad": ingresar_cantidad})
                cont += 1
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            titulos.append({"Nombre": fila["Nombre"], "Cantidad": int(float(fila["Cantidad"]))})
    
    return titulos
def mostrar_titulos():
    print("-----Listado de titulos-----")
    titulos= obtener_titulos()
    print("Nombre------------Cantidad")
    for titulo in titulos:
        print(f"{titulo['Nombre']} - {titulo['Cantidad']}")
def nuevos_titulos():
    print("-----Agregar nuevo titulo-----")
    Nombre=input("Ingrese el titulo: ").strip()
    if existe_titulo(Nombre):
        print("El titulo ya existe en el listado")
        return 
    Cantidad=input("Cantidad:")
    if validar_cantidad(Cantidad):
       print("La cantidad no es valida") 
       return
    Cantidad=float(Cantidad)
    agregarTitulo({'Nombre':Nombre, 'Cantidad':Cantidad})
    print("Se agrego correctamente")
def agregarTitulo(Nombre):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['Nombre','Cantidad'])
        escritor.writerow(Nombre)
def existe_titulo(Nombre):
    titulos=obtener_titulos()
    for titulo in titulos:
        if titulo['Nombre'].lower()==Nombre.strip().lower():
            return True
    return False
def modificar_ejemplares():
    titulos = obtener_titulos()
    Nombre = input("Ingrese el titulo del libro: ").strip()
    
    if not Nombre:
        print("No puede estar vacio")
        return
    
    encontrado = False
    for titulo in titulos:
        if titulo['Nombre'].lower() == Nombre.lower():
            Cantidad = input("Ingrese nueva cantidad: ").strip()
            if validar_cantidad(Cantidad):  
                print("La cantidad no es valida")
                return
            titulo["Cantidad"] = int(Cantidad)
            encontrado = True
            break
    
    if encontrado:
        guardarCantidad(titulos)
        print("Cantidad modificada correctamente")
    else:
        print("No se encuentra el titulo")
def validar_cantidad(Cantidad):
    if not Cantidad.isdigit():
        return True
def disponibilidad():
    titulos= obtener_titulos() 
    Nombre = input("Ingrese el titulo del libro: ").strip() 
    if not Nombre:
        print("No puede estar vacio")
        return
    encontrado = False
    for titulo in titulos:
        if titulo['Nombre'].lower() == Nombre.lower():
            encontrado = True
            if titulo['Cantidad'] == 0:
                print(f"El título '{titulo['Nombre']}' no tiene ejemplares disponibles")
            else:
                print(f"El título '{titulo['Nombre']}' tiene {titulo['Cantidad']} ejemplares")
            break
    
    if not encontrado:
        print("No se encuentra el titulo")
def listar_agotados():
    titulos=obtener_titulos()
    agotados=[]
    for titulo in titulos:
        if titulo['Cantidad']==0:
            agotados.append(titulo)
    if not agotados:
        print("No hay titulos agotados")
    else:
        for titulo in agotados:
            print("-----Agotados-----")
            print(titulo['Nombre'])
def prestamos():
    titulos=obtener_titulos()
    prestar=input("Titulo: ")
    encontrado=False
    for titulo in titulos:
        if titulo['Nombre'].lower()==prestar.lower():
            encontrado=True
            if titulo['Cantidad']==0:
                print("No hay ejemplares disponibles")
            else:
                titulo['Cantidad']-=1
                guardarCantidad(titulos)
                print(f"Prestamo  realizado. Quedan {titulo['Cantidad']} ejemplares disponibles.")
                break
    if not encontrado:
        print("No se encuentra el titulo")
def guardarCantidad(titulos):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['Nombre', 'Cantidad'])
        escritor.writeheader()
        escritor.writerows(titulos) 
def devoluciones():
    titulos=obtener_titulos()
    devolver=input("Titulo: ")
    encontrado=False
    for titulo in titulos:
        if titulo['Nombre'].lower()==devolver.lower():
            encontrado=True
            titulo['Cantidad']+=1
            guardarCantidad(titulos)
            print(f"Devolucion  realizada. Quedan {titulo['Cantidad']} ejemplares disponibles.")
            break   
    if not encontrado:
        print("No se encuentra el titulo")
def salir():
    print("Fin del programa")

obtener_titulos()
mostrar_menu()        