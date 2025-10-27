#-----Actividad 1-----
precios_frutas={'Banana':1200, 'Anana':2500, 'Melon':3000,'Uva':1450}
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300
print(precios_frutas)

#-----Actividad 2-----
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800
print(precios_frutas)

#-----Actividad 3-----
frutas=[precios_frutas.keys()]
print(frutas)

#-----Actividad 4-----
contactos={}
for i in range(5):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input(f"Ingrese el numero de {nombre}: ")
    contactos[nombre]= numero
Buscar=input("Buscar: ")
if Buscar not in contactos:
    print(f"{Buscar} no se encuentra en contactos")
else:
    print(contactos[Buscar])

 #-----Actividad 5-----
frase=input("Ingrese una frase: ")
palabras=set(frase.split())
print(palabras)
for i in palabras:
    print(f"{i}:{frase.count(i)}")

#-----Actividad 6-----
alumnos={}
for i in range(3):
    nombre=input("Alumno: ")
    n1=float(input("Nota1:"))
    n2=float(input("Nota2:"))
    n3=float(input("Nota3:"))
    notas=(n1,n2,n3)
    alumnos[nombre]=notas
for nombre, notas in alumnos.items():
    promedio=(notas[0]+notas[1]+notas[2])/len(notas)
    print(f"El promedio de {nombre} es {promedio}")

#-----Actividad 7-----
parcial1 = {"Acuña", "Cozzi", "Fabregat", "Zhang", "Zorzoli", "Bendjouya"}
parcial2 = {"Zorzoli", "Cozzi", "Bottaro", "Storich", "Acuña", "Abraldes"}
ambos=parcial1&parcial2
print(f"Estudiantes que aprobaron ambos examenes:{ambos}")
unico=parcial1^parcial2
print(f"Estudiantes que solo aprobaron un parcial:{unico}")

#-----Actividad 8-----
productos={"leche":15,"jabon":8,"fideos":6}
opcion=input("Presione 's' para ver stock. Presione 'p' para agregar un producto. Presione 'm' para modificar stock: ")
if opcion=="s":
    stock=input("Buscar: ")
    if stock in productos:
        print(f"stock de {stock}:{productos[stock]}" )
elif opcion=="p":
    nuevo=input("Nuevo producto:")
    cantidad=int(input("stock:"))
    productos[nuevo]=cantidad
    print(productos)
else:
    cambio=input("Producto:")
    nuevo_stock=int(input("nuevo stock:"))
    productos[cambio]=nuevo_stock
    print(productos)

#-----Actividad 9-----
agenda={("lunes","10:00"):"Reunion escolar",("martes","14:00"):"Alergista",("miercoles","11:30"):"Pilates"}
dia=input("dia:")
hora=input("hora:")
clave=(dia,hora)
if clave in agenda:
    print(agenda[clave])
else:
    print("Sin eventos")

#-----Actividad 10-----
original={"Argentina":"Buenos Aires","Paraguay":"Asuncion","Uruguay":"Montevideo"}
print(original)
inverso={capital:pais for pais, capital in original.items()}
print(inverso)