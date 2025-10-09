#-----Actividad 1-----
def imprimir_hola_mundo():
    print("Hola Mundo")


imprimir_hola_mundo()

#-----Actividad 2-----
def saludar_usuario(nombre):
    print(f"Hola, {nombre}")
nombre= input("Ingrese un nombre: ")
print(saludar_usuario(nombre))

#-----Actividad 3-----
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre= input("Nombre: ")
apellido= input("Apellido: ")
edad= int(input("Edad: "))
residencia= input("Residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))

#-----Actividad 4-----
def calcular_area_circulo(radio):
    area=  3.14*radio**2
    print(area)
def calcular_perimetro_circulo(radio):
    perimetro= 2*3.14*radio
    print(perimetro)
radio= int(input("Ingrese el radio: "))
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

#-----Actividad 5-----
def segundos_a_horas(segundos):
    horas= segundos/60
    print(f"{segundos} es igual a {horas} horas.")
segundos= float(input("Segundos: "))
print(segundos_a_horas(segundos))

#-----Actividad 6-----
def tabla_multiplicar(numero):
    cont=1
    while cont<=10:
        tabla= numero*cont
        print(tabla)
        cont+=1
numero= int(input("Numero: "))
print(tabla_multiplicar(numero))

#-----Actividad 7-----
def operaciones_basicas(a,b):
    suma= a+b
    resta= a-b
    multiplicacion= a*b
    division= a/b  
    return(suma, resta, multiplicacion, division)
a= int(input("Ingrese un numero: "))
b= int(input("Ingrese un numero: "))
resultados= operaciones_basicas(a,b)
print(f"Suma:{resultados[0]}\nResta:{resultados[1]}\nMultiplicacion:{resultados[2]}\nDivision:{resultados[3]}")

#-----Actividad 8-----
def calcular_imc(peso,altura):
    imc= peso/(altura**2)
    return imc
peso= float(input("Ingrese su peso en Kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))
resultado= calcular_imc(peso,altura)
print(f"IMC: {resultado:.2f}")

#-----Actividad 9-----
def celsius_a_farenheit(celsius):
    farenheit=  (celsius*9/5)+32
    return farenheit
celsius= int(input("Ingrese una temperatura en Celsius: "))
print(f"{celsius} grados Celsius equivalen a {celsius_a_farenheit(celsius)} Farenheits")

#-----Actividad 10-----
def calcular_promedio(a,b,c):
    promedio= (a+b+c)/3
    return promedio
a= int(input("Ingrese un numero: "))
b= int(input("Ingrese un numero: "))
c= int(input("Ingrese un numero: "))
print(f"Promedio: {calcular_promedio(a,b,c)}")