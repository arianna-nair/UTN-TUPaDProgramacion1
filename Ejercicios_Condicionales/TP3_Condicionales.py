#-----Actividad 1-----
edad= int(input("Ingrese su edad:"))
if edad > 18:
   print("Es mayor de edad.")
else:
    pass

#-----Actividad 2-----
nota=int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#-----Actividad 3-----
numero= int(input("Ingrese un numero:"))
if numero % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

#-----Actividad 4-----
edad= int(input("Ingrese su edad:"))
if edad<12:
    print("Niño/a")
elif edad >=12 and edad <18:
    print("Adolescente")
elif edad >=18 and edad <30:
   print("Adulto/a joven")
else:
    print("Adulto/a")

#-----Actividad 5-----
contraseña= input("Introduzca una contraseña:")
long_contraseña= len(contraseña)
if long_contraseña >=8 and long_contraseña <=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")

#-----Actividad 6-----
import random
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
from statistics import mode,median,mean
mode_num= mode(numeros_aleatorios)
med_num= median(numeros_aleatorios)
mean_num= mean(numeros_aleatorios)
if mean_num>med_num and med_num>mode_num:
    print("Sesgo positivo")
elif mean_num<med_num and med_num<mode_num:
    print("Sesgo negativo")
elif mean_num==med_num and mean_num==mode_num:
    print("No hay sesgo")
else:
    pass

#-----Actividad 7-----
palabra= input("Ingrese una palabra o frase:")
if palabra[-1].lower() in "aeiou":
    print(f"{palabra} !")
else:
    print(palabra)

#-----Actividad 8-----
nombre= input("Ingrese su nombre y elija la opcion que desee:")
opcion= int(input("1. Si quiere su nombre en mayusculas. \n2. Si quiere su nombre en minusculas. \n3. Si quiere su nombre con la primera letra mayuscula."))
if opcion==1:
    nombre_mayus= nombre.upper()
    print(nombre_mayus)
elif opcion==2:
    nombre_minus= nombre.lower()
    print(nombre_minus)
else:
    nombre_title= nombre.title()
    print(nombre_title)

#-----Actividad 9-----
magnitud= int(input("Ingrese la magnitud del terremoto:"))
if magnitud<3:
    print("Muy leve (Imperceptible)")
elif magnitud>=3 and magnitud <4:
    print("Leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños.)")
elif magnitud >=5 and magnitud <6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud >=7:
    print("Extremo(puede causar graves daños a gran escala)")
else:
    pass

#-----Actividad 10-----
hemisferio= input("En que hemisferio se encuentra N/S:")
mes= (input("En que mes se encuentra:"))
dia= int(input("Que dia es:"))
if (dia>=21 or dia<=20) and (mes=="diciembre" or mes=="enero" or mes=="febrero" or mes=="marzo") and hemisferio == "N":
    print("Invierno")
elif (dia>=21 or dia<=20) and (mes=="diciembre" or mes=="enero" or mes=="febrero" or mes=="marzo") and hemisferio == "S":
    print("Verano")
elif (dia>=21 or dia<=20) and (mes=="marzo" or mes=="abril" or mes=="mayo" or mes=="junio") and hemisferio == "N":
    print("Primavera")
elif (dia>=21 or dia<=20) and (mes=="marzo" or mes=="abril" or mes=="mayo" or mes=="junio") and hemisferio == "S":
    print("Otoño")
elif (dia>=21 or dia<=20) and (mes=="junio" or mes=="julio" or mes=="agosto" or mes=="septiembre") and hemisferio == "N":
    print("Verano")
elif (dia>=21 or dia<=20) and (mes=="junio" or mes=="julio" or mes=="agosto" or mes=="septiembre") and hemisferio == "S":
    print("Invierno")
elif (dia>=21 or dia<=20) and (mes=="septiembre" or mes=="octubre" or mes=="noviembre" or mes=="diciembre") and hemisferio == "N":
    print("Otoño")
    elif (dia>=21 or dia<=20) and (mes=="septiembre" or mes=="octubre" or mes=="noviembre" or mes=="diciembre") and hemisferio == "S":
    print("Primavera")