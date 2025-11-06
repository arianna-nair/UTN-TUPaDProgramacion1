import csv
import os

NOMBRE_ARCHIVO = "paises.csv"

def lista_paises():
    paises = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Pais", "Poblacion", "Superficie", "Continente"])
            escritor.writeheader()
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append({"Pais": fila["Pais"], "Poblacion": int(fila["Poblacion"]), "Superficie": int(fila["Superficie"]), "Continente": fila["Continente"]})
    return paises

def guardar_paises(paises):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["Pais", "Poblacion", "Superficie", "Continente"])
        escritor.writeheader()
        escritor.writerows(paises)

def mostrar_menu():
    while True:
        print("\n-----------Menu de opciones-----------")
        opcion = input("1.Agregar un pais\n2.Actualizar datos de poblacion y superficie\n3.Buscar pais\n4.Filtrar paises\n5.Ordenar paises\n6.Estadisticas\n7.Salir\nOpcion: ")
        match opcion:
            case "1":
                agregar_pais()
            case "2":
                actualizar_datos()
            case "3":
                buscar_pais()
            case "4":
                filtros()
            case "5":
                ordenar_paises()
            case "6":
                estadisticas()
            case "7":
                print("Salir")
                break
            case _:
                print("La opcion no es valida")

def agregar_pais():
    print("-----Agregar pais-----")
    pais = input("Pais: ").strip()
    if not pais:
        print("El campo pais no puede estar vacio")
        return
    if existe_pais(pais):
        print(f"{pais} ya existe en el listado.")
        return
    
    poblacion = input("Poblacion: ").strip()
    if not poblacion or not poblacion.isdigit() or int(poblacion) <= 0:
        print("La poblacion debe ser un numero positivo")
        return
    
    superficie = input("Superficie en KM2: ").strip()
    if not superficie or not superficie.isdigit() or int(superficie) <= 0:
        print("La superficie debe ser un numero positivo")
        return
    
    continente = input("Continente: ").strip()
    if not continente:
        print("El campo continente no puede estar vacio")
        return
    
    agregarPais({'Pais': pais, 'Poblacion': int(poblacion), 'Superficie': int(superficie), 'Continente': continente})
    print("Se agrego correctamente")

def existe_pais(pais):
    paises = lista_paises()
    for p in paises:
        if p['Pais'].lower() == pais.strip().lower():
            return True
    return False

def agregarPais(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['Pais', 'Poblacion', 'Superficie', 'Continente'])
        escritor.writerow(pais)

def actualizar_datos():
    paises = lista_paises()
    opcion = input("1.Actualizar poblacion\n2.Actualizar superficie\nOpcion: ")
    match opcion:
        case "1":
            actualizarPoblacion()
        case "2":
            actualizarSuperficie()
        case _:
            print("Opcion invalida")

def actualizarPoblacion():
    paises = lista_paises()
    buscar = input("Buscar pais: ").strip()
    if not buscar:
        print("No puede estar vacio")
        return
    
    encontrado = False
    for pais in paises:
        if pais['Pais'].lower() == buscar.lower():
            encontrado = True
            poblacion = input("Poblacion actualizada: ").strip()
            if not poblacion or not poblacion.isdigit() or int(poblacion) <= 0:
                print("La poblacion debe ser un numero positivo")
                return
            pais['Poblacion'] = int(poblacion)
            guardar_paises(paises)
            print("Poblacion actualizada")
            break
    
    if not encontrado:
        print(f"{buscar} no esta en la lista")

def actualizarSuperficie():
    paises = lista_paises()
    buscar = input("Buscar pais: ").strip()
    if not buscar:
        print("No puede estar vacio")
        return
    
    encontrado = False
    for pais in paises:
        if pais['Pais'].lower() == buscar.lower():
            encontrado = True
            superficie = input("Superficie actualizada: ").strip()
            if not superficie or not superficie.isdigit() or int(superficie) <= 0:
                print("La superficie debe ser un numero positivo")
                return
            pais['Superficie'] = int(superficie)
            guardar_paises(paises)
            print("Superficie actualizada")
            break
    
    if not encontrado:
        print(f"{buscar} no esta en la lista")

def buscar_pais():
    paises = lista_paises()
    buscar = input("Buscar pais: ").strip()
    if not buscar:
        print("No puede estar vacio")
        return
    
    encontrado = False
    for pais in paises:
        if buscar.lower() in pais['Pais'].lower():
            encontrado = True
            print(f"\nPais: {pais['Pais']}")
            print(f"Poblacion: {pais['Poblacion']}")
            print(f"Superficie: {pais['Superficie']} KM2")
            print(f"Continente: {pais['Continente']}")
            print("-" * 40)
    
    if not encontrado:
        print(f"No se encontraron paises con '{buscar}'")

def filtros():
    opcion = input("1.Filtrar por continente\n2.Filtrar por poblacion\n3.Filtrar por Superficie\nOpcion: ")
    match opcion:
        case "1":
            filtroContinente()
        case "2":
            filtroPoblacion()
        case "3":
            filtroSuperficie()
        case _:
            print("Opcion invalida")

def filtroContinente():
    paises = lista_paises()
    buscar_continente = input("Continente: ").strip()
    if not buscar_continente:
        print("No puede estar vacio")
        return
    
    encontrado = False
    for pais in paises:
        if pais['Continente'].lower() == buscar_continente.lower():
            encontrado = True
            print(f"{pais['Pais']} - Poblacion: {pais['Poblacion']} - Superficie: {pais['Superficie']} KM2")
    
    if not encontrado:
        print(f"No se encontraron paises en {buscar_continente}")

def filtroPoblacion():
    paises = lista_paises()
    menores = []
    mayores = []
    
    for pais in paises:
        if pais['Poblacion'] <= 15000000:
            menores.append(pais)
        else:
            mayores.append(pais)
    
    print("\n-----Poblaciones menores o iguales a 15.000.000-----")
    if menores:
        for pais in menores:
            print(f"{pais['Pais']} - Poblacion: {pais['Poblacion']}")
    else:
        print("No hay paises en esta categoria")
    
    print("\n-----Poblaciones mayores a 15.000.000-----")
    if mayores:
        for pais in mayores:
            print(f"{pais['Pais']} - Poblacion: {pais['Poblacion']}")
    else:
        print("No hay paises en esta categoria")

def filtroSuperficie():
    paises = lista_paises()
    menores = []
    mayores = []
    
    for pais in paises:
        if pais['Superficie'] <= 2000000:
            menores.append(pais)
        else:
            mayores.append(pais)
    
    print("\n-----Superficies menores o iguales a 2.000.000 KM2-----")
    if menores:
        for pais in menores:
            print(f"{pais['Pais']} - Superficie: {pais['Superficie']} KM2")
    else:
        print("No hay paises en esta categoria")
    
    print("\n-----Superficies mayores a 2.000.000 KM2-----")
    if mayores:
        for pais in mayores:
            print(f"{pais['Pais']} - Superficie: {pais['Superficie']} KM2")
    else:
        print("No hay paises en esta categoria")

def ordenar_paises():
    paises = lista_paises()
    if not paises:
        print("No hay paises registrados")
        return
    
    opcion = input("1.Ordenar por nombre\n2.Ordenar por poblacion\n3.Ordenar por superficie\nOpcion: ")
    if opcion not in ["1", "2", "3"]:
        print("Opcion invalida")
        return
    
    orden = input("Ascendente (A) o Descendente (D): ").strip().upper()
    if orden not in ["A", "D"]:
        print("Orden invalido")
        return
    
    reverso = (orden == "D")
    
    def obtener_pais_lower(x):
        return x['Pais'].lower()
    
    def obtener_poblacion(x):
        return x['Poblacion']
    
    def obtener_superficie(x):
        return x['Superficie']
    
    match opcion:
        case "1":
            paises_ordenados = sorted(paises, key=obtener_pais_lower, reverse=reverso)
        case "2":
            paises_ordenados = sorted(paises, key=obtener_poblacion, reverse=reverso)
        case "3":
            paises_ordenados = sorted(paises, key=obtener_superficie, reverse=reverso)
    
    print("\n--- Paises ordenados ---")
    for pais in paises_ordenados:
        print(f"{pais['Pais']} - Poblacion: {pais['Poblacion']} - Superficie: {pais['Superficie']} KM2")

def estadisticas():
    paises = lista_paises()
    if not paises:
        print("No hay paises registrados")
        return
    
    opcion = input("1.Maximos y minimos de poblacion\n2.Promedio de poblacion\n3.Promedio de superficie\n4.Paises por continente\nOpcion: ")
    match opcion:
        case "1":
            MaxMin(paises)
        case "2":
            PromPoblacion(paises)
        case "3":
            PromSuperficie(paises)
        case "4":
            PaisesContinente(paises)
        case _:
            print("Opcion invalida")

def MaxMin(paises):
    def obtener_poblacion(x):
        return x['Poblacion']
    
    pais_max = max(paises, key=obtener_poblacion)
    pais_min = min(paises, key=obtener_poblacion)
    print(f"\nMayor poblacion: {pais_max['Pais']} con {pais_max['Poblacion']} habitantes")
    print(f"Menor poblacion: {pais_min['Pais']} con {pais_min['Poblacion']} habitantes")

def PromPoblacion(paises):
    total = sum(p['Poblacion'] for p in paises)
    promedio = total / len(paises)
    print(f"\nPromedio de poblacion: {promedio:.2f} habitantes")

def PromSuperficie(paises):
    total = sum(p['Superficie'] for p in paises)
    promedio = total / len(paises)
    print(f"\nPromedio de superficie: {promedio:.2f} KM2")

def PaisesContinente(paises):
    continentes = {}
    for pais in paises:
        cont = pais['Continente'].strip().lower()
        nombre = pais['Pais']
        
        if cont not in continentes:
            continentes[cont] = []
        continentes[cont].append(nombre)
    print("\nPaíses por continente:")
    for continente in sorted(continentes.keys()):
        print(f"\n{continente}:")
        for pais in continentes[continente]:
            print(f"  - {pais}")
        print(f"Total: {len(continentes[continente])} país(es)")

mostrar_menu()