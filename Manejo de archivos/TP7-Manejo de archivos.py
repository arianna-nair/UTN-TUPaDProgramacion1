#-----Actividad 1-----
lineas=["producto|precio|cantidad\n"
"lapicera|120.50|30\n"
"cartuchera|350|5\n"
"cuaderno|560|15\n"]
with open("productos.txt","w") as archivo:
    archivo.writelines(lineas)
#-----Actividad 2-----
with open("productos.txt","r") as archivo:
    linea=archivo.readlines()
    for i in linea:
        partes=i.strip().split("|")
        print(partes)
#-----Actividad 3-----
nuevo=input("Ingrese nuevo producto:")
precio=float(input("Precio:"))
cantidad=int(input("Cantidad: "))
agregar=nuevo + "|" + str(precio) + "|" + str(cantidad)
with open("productos.txt","a") as archivo:
    archivo.write(agregar+"\n")
#-----Actividad 4-----
productos = []
with open("productos.txt", "r") as archivo:
    lineas_leidas = archivo.readlines()
    for i in range(1, len(lineas_leidas)):
        partes = lineas_leidas[i].strip().split("|")
        producto = {"nombre": partes[0],"precio": float(partes[1]),"cantidad": int(partes[2])}
        productos.append(producto)
#-----Actividad 5-----
buscar = input("Buscar: ")
print("Buscando:", buscar)
print("Lista de productos:", productos)
encontrado = False
for producto in productos:
    print("Comparando con:", producto["nombre"])
    if producto["nombre"] == buscar:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Error: Producto no encontrado")
#-----Actividad 6-----
with open("productos.txt", "w") as archivo:
    archivo.write("producto|precio|cantidad\n")
    for producto in productos:
        linea = f"{producto['nombre']}|{producto['precio']}|{producto['cantidad']}\n"
        archivo.write(linea)