#-----Actividad 1-----
notas=[10, 8.5, 7, 4.7, 6, 9, 2, 9.5, 7.6, 8]
suma=0
for i in notas:
    print (i, end="\n") 
for i in notas:
    suma+=i
    promedio=suma/len(notas)
print("Promedio: ", promedio)
cantidad_elementos= len(notas)
for indice_pasada in range (cantidad_elementos -1):
    for indice_actual in range (cantidad_elementos - 1 - indice_pasada):
        if notas[indice_actual]>notas[indice_actual+1]:
            notas[indice_actual], notas[indice_actual+1]= notas[indice_actual+1], notas[indice_actual]
print("Menor:", notas[0], "\n Mayor:", notas[9])

#-----Actividad 2-----
productos=[]
for i in range(5):
    elemento= input("Ingrese un elemento:" )
    productos.append(elemento)
productos_modificado=sorted(productos)
print(productos_modificado)
eliminar_producto= input("¿Que producto desea eliminar?:" )
productos_modificado.remove(eliminar_producto)
print(productos_modificado)

#-----Actividad 3-----
numeros_azar=[2,14,63,78,95,3,41,35,74,90,57,88,69,32,29]
pares=[]
impares=[]
for i in numeros_azar:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Pares:", pares, "Impares:",impares)

#-----Actividad 4-----
datos=[1,3,5,3,7,1,9,5,3]
datos_sin_repetir=[]
for i in datos:
    if i not in datos_sin_repetir:
        datos_sin_repetir.append(i)
print(datos_sin_repetir)

#-----Actividad 5-----
alumnos=["Arianna","Martina","Lara","Lucia","Pablo","Rocio","Paulina","Agustin"]
print(alumnos)
modificar= input("Desea agregar o eliminar a algun estudiante? s/n: ")
if modificar == "s":
    tipo= input("agregar/eliminar:")
    if tipo=="agregar":
        agregar=input("Ingrese el nombre:")
        alumnos.append(agregar)
    elif tipo=="eliminar":
         eliminar=input("Ingrese el nombre:")
         alumnos.remove(eliminar)
    else:
        print("Error")
print(alumnos)

#-----Actividad 6-----
numeros=[1,2,3,4,5,6,7]
ultimo=numeros[-1]
lista_rotada=[0]*len(numeros)
for i in range (len(numeros)):
 #   if i==0:
        lista_rotada[i]=ultimo
    else:
        lista_rotada[i]=numeros[i-1]
print(lista_rotada)

#-----Actividad 7-----
temperaturas = [
    [12, 22],  # Día 1
    [10, 24],  # Día 2
    [14, 25],  # Día 3
    [11, 20],  # Día 4
    [13, 27],  # Día 5
    [9, 19],   # Día 6
    [15, 26]   # Día 7
]
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]
promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)
print("Promedio de mínimas:", promedio_min)
print("Promedio de máximas:", promedio_max)
amplitudes = [dia[1] - dia[0] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1  
print("Mayor amplitud térmica:", mayor_amplitud, "°C")
print("Se registró en el día:", dia_mayor)
                                
#-----Actividad 8-----
notas=[[10,8,9],
       [9,6,8],
       [5,6,3],
       [8,7,6],
       [9,9.5,8]
       ]
for i in range(len(notas)):
    suma_alumno = 0
    for j in range(len(notas[i])):
        suma_alumno += notas[i][j]
    promedio_alumno = suma_alumno / len(notas[i])
    print("El promedio del alumno ", i+1, "es:", promedio_alumno)
    num_alumnos = len(notas)
num_materias = len(notas[0])
for x in range(num_materias):
    suma_materia = 0
    for i in range(num_alumnos):
        suma_materia += notas[i][x]
    promedio_materia = suma_materia / num_alumnos
print("El promedio de la materia ", x+1, "es:", promedio_materia)

#-----Actividad 9-----
tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]
for fila in tablero:
    for casilla in fila:
        print(casilla, end=" ")
    print("\n", end="")
jugador = "X"
for turno in range(9):
    print("Turno del jugador", jugador)
    casilla_valida = False
    while casilla_valida == False:
        fila = int(input("Ingresá fila (0-2): "))
        col = int(input("Ingresá columna (0-2): "))
        if tablero[fila][col] == "-":
            tablero[fila][col] = jugador
            casilla_valida = True
        else:
            print("Casilla ocupada, elegí otra.")
    for f in tablero:
        for casilla in f:
            print(casilla, end=" ")
        print("\n", end="")
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

#-----Actividad 10----
ventas = [
    [10, 12, 11, 9, 8, 10, 15],   # Producto 1
    [5, 7, 6, 5, 8, 6, 7],        # Producto 2
    [20, 18, 25, 22, 19, 20, 21], # Producto 3
    [7, 9, 8, 10, 6, 5, 7]        # Producto 4
]
print("Total vendido por producto:")
totales_productos = []
for i in range(len(ventas)):
    suma_producto = 0
    for j in range(len(ventas[i])):
        suma_producto += ventas[i][j]
    totales_productos.append(suma_producto)
    print("Producto", i+1, ":", suma_producto)
totales_dias = []
for j in range(len(ventas[0])):
    suma_dia = 0
    for i in range(len(ventas)):
        suma_dia += ventas[i][j]
    totales_dias.append(suma_dia)
mayor_venta = totales_dias[0]
dia_mayor = 0
for j in range(1, len(totales_dias)):
    if totales_dias[j] > mayor_venta:
        mayor_venta = totales_dias[j]
        dia_mayor = j
print("\nDía con mayores ventas totales: Día", dia_mayor+1, "con", mayor_venta, "ventas")
mayor_producto = totales_productos[0]
prod_mayor = 0
for i in range(1, len(totales_productos)):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        prod_mayor = i
print("Producto más vendido en la semana: Producto", prod_mayor+1, "con", mayor_producto, "ventas")
