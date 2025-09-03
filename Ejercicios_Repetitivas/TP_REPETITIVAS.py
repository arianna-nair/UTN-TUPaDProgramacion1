#-----Actividad 1-----
cont=0
while cont <= 100:
    if cont % 2 == 0:
        print(cont)
    cont+=1

#-----Actividad 2-----
digitos=0
num= int(input("Ingrese un numero entero:"))
while num >0:
    num= num//10
    digitos+=1
print(digitos)
#-----Actividad 3-----
inicio= int(input("Ingrese un valor inicial:"))
fin= int(input("Ingrese un valor final:"))
acumulador= 0
for i in range (inicio,fin):
    if i==inicio:
        continue
    acumulador += i
print(acumulador)

#-----Actividad 4-----
acumulador = 0
while acumulador >=0:
    num= int(input("Ingrese un numero:"))
    acumulador += num
    if num==0:
        break
print(acumulador)

#-----Actividad 5-----
num= int(input("Adivine el numero entre 0 y 9:"))
predeterminado=7
intentos=0
while num!=predeterminado:
    intentos+=1
    num= int(input("Vuelva a intentar:"))
    if num==predeterminado:
        break
print("Intentos:", intentos)

#-----Actividad 6-----
for i in range (100,0,-1):
    if i % 2 == 0:
        print(i)

#-----Actividad 7-----
num=int(input("Ingrese un numero positivo:"))
acumulador=0
for i in range (num):
    acumulador+=i
print(acumulador)

#-----Actividad 8-----
acu_pares=0 #Acumula los numeros pares
acu_impares= 0 #Acumula los numeros impares
acu_positivos= 0 #Acumula los numeros positivos
acu_negativos= 0#Acumula los numeros negativos
for i in range (100):
    num=int(input("Ingrese un numero:"))
    if num % 2 == 0:
        acu_pares +=1
    else:
        acu_impares +=1
    if num<0:
         acu_negativos+=1
    else:
         acu_positivos+=1
print(f" Pares:{acu_pares} \n Impares: {acu_impares} \n Positivos: {acu_positivos} \n Negativos: {acu_negativos}")

#-----Actividad 9-----
cont=0
acumulador=0
for i in range (2):
    num= int(input("Ingrese un numero:"))
    acumulador+=num
    cont+=1
print(f"Promedio: {(acumulador/cont)}")

#-----Actividad 10-----
num=int(input("Ingrese un numero:"))
invertido=0
while num>0:
    digito= num%10
    invertido= invertido*10+digito
    num= num//10
    if num < 0:
        invertido= - invertido
print("Numero invertido:", invertido)