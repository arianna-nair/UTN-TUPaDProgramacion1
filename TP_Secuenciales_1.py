#------Actividad 1------
print("Hola, Mundo!")

#------Actividad 2------
nombre=input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

#------Actividad 3------
nombre=input("Nombre:")
apellido=input("Apellido:")
edad=int(input("Edad:"))
residencia=input("Lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#------Actividad 4------
radio=float(input("Ingrese el radio del círculo:"))
import math
area= math.pi*(radio**2)
perimetro=2*math.pi*radio
print("area:", area)
print("Perímetro: ", perimetro)

#------Actividad 5------
segundos= int(input("Ingrese una cantidad de segundos:"))
hora= segundos*1/3600
print(f"{segundos} es igual a {hora} hora/s")

#------Actividad 6------
numero=int(input("Ingrese un número:"))
print(numero, "x 1=", numero*1)
print(numero, "x 1=", numero*2)
print(numero, "x 1=", numero*3)
print(numero, "x 1=", numero*4)
print(numero, "x 1=", numero*5)
print(numero, "x 1=", numero*6)
print(numero, "x 1=", numero*7)
print(numero, "x 1=", numero*8)
print(numero, "x 1=", numero*9)
print(numero, "x 1=", numero*10)

#------Actividad 7------
print("Ingrese 2 números diferentes de 0 (cero)")
num1= int(input())
num2= int(input())
print("suma=", num1+num2)
print("division=", num1/num2)
print("multiplicacion=", num1*num2)
print("resta=", num1-num2)

#------Actividad 8------
peso= float(input("Peso (Kg):"))
altura= float(input("Altura (m):"))
IMC= peso/(altura**2)
print(f"Su IMC es {IMC}")

#------Actividad 9------
celsius=float(input("Ingrese grados Celsius:"))
fahr= (9 % 5)*celsius+32
print(f"La Temperatura en Fahrenheits de {celsius} Celsius es {fahr}.")

#------Actividad 10------
print("Ingrese 3 números")
num1= float(input())
num2=float(input())
num3=float(input())
promedio= (num1+num2+num3)/3
print(f"Promedio:{promedio}")